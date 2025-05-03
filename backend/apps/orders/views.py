from django.db.models import Count
from django.utils.decorators import method_decorator

from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.permissions.is_superuser_permission import IsSuperUser
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from .filters import OrderFilter
from .models import OrdersModel
from .serializers import AssignOrderToManagerSerializer, CommentsSerializer, OrderSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='get all orders'))
class OrderListView(generics.ListAPIView):
    '''
        Show all orders
    '''
    queryset = OrdersModel.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = OrderFilter


@method_decorator(name='post', decorator=swagger_auto_schema(operation_id='add manager to chosen order'))
class AssignedOrderToManager(generics.GenericAPIView):
    '''
        Assign order to manager
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


@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='get manager order'))
class GetMyOrdersView(generics.ListAPIView):
    '''
        show all orders of authenticated manager
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return OrdersModel.objects.filter(manager=user)


@method_decorator(name='post', decorator=swagger_auto_schema(operation_id='manager can create comments to order'))
class CommentOrderCreateView(generics.GenericAPIView): # in work
    permission_classes = (IsAuthenticated,)
    queryset = OrdersModel.objects.all()
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


class UpdateOrderView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    pass # todo

@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='get general orders statistics'))
class GetGeneralOrdersStatisticsView(generics.GenericAPIView):
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
                by_status['Unknown'] = null_count

        return Response({
            'total_orders': total_orders,
            'by_status': by_status},
            status.HTTP_200_OK)




