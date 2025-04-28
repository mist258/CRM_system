from django.utils.decorators import method_decorator

from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils.representation import serializer_repr

from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from .filters import OrderFilter
from .models import OrdersModel
from .serializers import AssignOrderToManagerSerializer, OrderSerializer


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
class AssignedOrderToManager(generics.GenericAPIView): # in work
    '''
        Assign order to manager
    '''
    permission_classes = (IsAuthenticated,)
    queryset = OrdersModel.objects.all()
    serializer_class = AssignOrderToManagerSerializer

    def post(self, request, *args, **kwargs):
        order = self.get_object()
        user = self.request.user

        if order.manager is not None or order.status != "New":
            return Response({"detail": "You can't assign order to manager"},
                            status=status.HTTP_400_BAD_REQUEST)

        order.manager = user
        order.status = "In work"
        order.save()

        serializer = OrderSerializer(order)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetMyOrdersView(generics.RetrieveAPIView):
    '''
        show all orders of authenticated manager
    '''
    permission_classes = (IsAuthenticated,)
    pass # todo


class CommentOrderCreateView(generics.GenericAPIView):
    pass # todo perform_create / update

