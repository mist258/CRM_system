from django.contrib.auth import get_user_model
from django.db.models import Count
from django.utils.decorators import method_decorator

from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.permissions.is_order_owner import IsOrderOwner
from core.permissions.is_superuser_permission import IsSuperUser
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from .filters import OrderFilter
from .models import GroupModel, OrdersModel
from .serializers import OrderSerializer

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
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = OrderFilter


@method_decorator(name='put', decorator=swagger_auto_schema(operation_id='update order by id'))
class UpdateOrderView(generics.GenericAPIView):
    '''
        manager can update order
        (for authenticated manager)
    '''
    permission_classes = ( IsAuthenticated, IsOrderOwner, )
    serializer_class = OrderSerializer

    def put(self, request, *args, **kwargs):
        order = get_object_or_404(OrdersModel, pk=self.kwargs['order_pk'])
        user = self.request.user
        self.check_object_permissions(request, order)

        group = get_object_or_404(GroupModel, pk=self.kwargs['group_pk'])


        if order.manager == user and order.status is not None:
            order.manager = user
            order.status = 'In work'
            order.group = group
            order.save()

        else:
            return Response({"detail": "Another manager has been "
                                       "assigned to this order"},
                                status.HTTP_400_BAD_REQUEST)

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
