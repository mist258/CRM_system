from django.contrib.auth import get_user_model
from django.db.models import Count
from django.utils.decorators import method_decorator

from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.permissions.is_order_owner import IsOrderOwner
from core.permissions.is_superuser_permission import IsSuperUser
from django_filters.rest_framework import DjangoFilterBackend
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from drf_yasg.utils import swagger_auto_schema

from .filters import OrderFilter
from .models import GroupModel, OrdersModel
from .serializers import OrderSerializer

UserModel = get_user_model()


@method_decorator(name='list', decorator=swagger_auto_schema(operation_id='get all orders'))
class OrderViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    '''
        Show all orders with filters
        or selected by a specific id
        (for authenticated users)
    '''
    queryset = OrdersModel.objects.select_related('manager', 'group').prefetch_related('comments').all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = OrderFilter

    @method_decorator(name='get', decorator=swagger_auto_schema(operation_id='export all orders'))
    @action(detail=False, methods=['get'], renderer_classes=[XLSXRenderer])
    def orders_to_excel(self, request):
        '''
            export all orders to excel
            (for authenticated users)
        '''
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, headers={
            'Content-Disposition': 'attachment; filename="orders.xlsx"'
        })


@method_decorator(name='put', decorator=swagger_auto_schema(operation_id='update order by id'))
class UpdateOrderView(generics.UpdateAPIView):
    '''
        manager can update order
        (for authenticated manager)
    '''
    permission_classes = ( IsAuthenticated, IsOrderOwner, )
    serializer_class = OrderSerializer
    queryset = OrdersModel.objects.all()


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
