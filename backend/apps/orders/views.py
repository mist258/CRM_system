from django.contrib.auth import get_user_model
from django.db.models import Count
from django.utils.decorators import method_decorator

from rest_framework import generics, mixins, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.permissions.is_order_owner import IsOrderOwner
from core.permissions.is_superuser_permission import IsSuperUser
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from .filters import OrderFilter
from .models import GroupModel, OrdersModel
from .serializers import (
    AssignOrderToManagerSerializer,
    CommentsSerializer,
    GroupSerializer,
    ManagerStatisticsSerializer,
    OrderSerializer,
)

UserModel = get_user_model()


@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='get all orders'))
class OrderListView(generics.ListAPIView):
    '''
        Show all orders
        (for authenticated users)
    '''
    queryset = OrdersModel.objects.select_related('manager', 'group').prefetch_related('comments').all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = OrderFilter
    search_fields = ['email', 'phone', 'surname']


@method_decorator(name='post', decorator=swagger_auto_schema(operation_id='add manager to chosen order'))
class AssignedOrderToManager(generics.GenericAPIView):
    '''
        Assign order to manager
        (for authenticated manager)
    '''
    permission_classes = (IsAuthenticated,)
    queryset = OrdersModel.objects.all()
    serializer_class = AssignOrderToManagerSerializer

    def post(self, request, *args, **kwargs):
        order = self.get_object()
        user = self.request.user

        if order.manager is not None or (order.status not in ["New", None]):
            return Response({"detail": "Another manager has been "
                                       "assigned to this order"},
                            status.HTTP_400_BAD_REQUEST)

        order.manager = user
        order.status = "In work"
        order.save() 
        serializer = OrderSerializer(order)
        return Response(serializer.data, status.HTTP_201_CREATED)


@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='get manager order',
                                                            responses={200: OrderSerializer()}))
class GetMyOrdersView(generics.ListAPIView):
    '''
        show all orders of authenticated manager
        (for authenticated manager)
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return OrdersModel.objects.filter(manager=user)


@method_decorator(name='post', decorator=swagger_auto_schema(operation_id='manager can create comments to order'))
class CommentOrderCreateView(generics.GenericAPIView):
    '''
        manager can create comments to order
        (for authenticated manager)
    '''
    permission_classes = (IsAuthenticated,)
    queryset = OrdersModel.objects.prefetch_related('comments').all()
    serializer_class = CommentsSerializer

    def post(self, request, *args, **kwargs):
        order = self.get_object()
        user = self.request.user
        data =  self.request.data

        if order.manager is not None and order.manager != user:
            return Response({"detail": "Another manager has been "
                             "assigned to this order"}, status.HTTP_400_BAD_REQUEST)

        if order.manager is None:
            order.manager = user
            order.status = "In work"
            order.save()

        serializer = CommentsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(order=order)
        comment_serializer = OrderSerializer(order)
        return Response(comment_serializer.data, status.HTTP_201_CREATED)


@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='get all groups'))
@method_decorator(name='post', decorator=swagger_auto_schema(operation_id='create group'))
class CreateListGroupView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    '''
        create new group or list all groups
        (for authenticated manager)
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = GroupSerializer
    queryset = GroupModel.objects.all()

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='get group by id'))
class RetrieveGroupView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    '''
        retrieve group by id
        (for authenticated manager)
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = GroupSerializer
    queryset = GroupModel.objects.all()

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


@method_decorator(name='put', decorator=swagger_auto_schema(operation_id='update order by id'))
class UpdateOrderView(generics.GenericAPIView):
    '''
        manager can update order
        (for authenticated manager)
    '''
    permission_classes = (IsAuthenticated, IsOrderOwner,)
    serializer_class = OrderSerializer

    def put(self, request, *args, **kwargs):
        order = get_object_or_404(OrdersModel, pk=self.kwargs['order_pk'])
        self.check_object_permissions(request, order)

        group = get_object_or_404(GroupModel, pk=self.kwargs['group_pk'])

        order.group = group
        order.save()

        if request.data:
            serializer = self.get_serializer(order, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(order=order)

        result = OrderSerializer(order)
        return Response(result.data, status.HTTP_200_OK)


@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='get general orders statistics'))
class GeneralOrdersStatisticsView(generics.GenericAPIView):
    '''
     show general orders statistics
     (for admin)
    '''
    permission_classes = (IsSuperUser,)

    def get(self, request, *args, **kwargs):
        total_orders = OrdersModel.objects.count()
        status_count = (OrdersModel.objects.exclude(status__isnull=True)
                        .values('status')
                        .annotate(count=Count('status')))

        by_status = {}
        total_known = 0
        for item in status_count:
            status_name = item['status']
            by_status[status_name] = item['count']
            total_known += item['count']

            null_count = total_orders - total_known
            if null_count > 0:
                by_status['Null'] = null_count

        return Response({
            'total_orders': total_orders,
            'by_status': by_status},
            status.HTTP_200_OK)


@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='get manager orders statistics'))
class  OrderStatisticsByManagerView(generics.ListAPIView):
    '''
     show general orders statistics by each manager
     (for admin)
    '''
    serializer_class = ManagerStatisticsSerializer
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        return UserModel.objects.select_related('profile').filter(orders__isnull=False).distinct()
