from django.utils.decorators import method_decorator

from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from .filters import OrderFilter
from .models import OrdersModel
from .serializers import OrderSerializer


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

class AssignedOrderToManager(generics.GenericAPIView):
    '''
        Assign order to manager
    '''
    permission_classes = (IsAuthenticated,)
    pass # todo

class GetMyOrdersView(generics.RetrieveAPIView):
    '''
        show all orders of authenticated manager
    '''
    permission_classes = (IsAuthenticated,)
    pass # todo


class CommentOrderCreateView(generics.GenericAPIView):
    pass # todo perform_create / update

