from rest_framework import generics

from .models import OrdersModel
from .serializers import OrderSerializer


class OrderListView(generics.ListAPIView):
    queryset = OrdersModel.objects.all()
    serializer_class = OrderSerializer
