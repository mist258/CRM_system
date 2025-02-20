from django.utils.decorators import method_decorator

from rest_framework import generics

from drf_yasg.utils import swagger_auto_schema

from .models import OrdersModel
from .serializers import OrderSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='get all orders'))
class OrderListView(generics.ListAPIView):
    '''
        Show all orders
    '''
    queryset = OrdersModel.objects.all()
    serializer_class = OrderSerializer
