from django.utils.decorators import method_decorator

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.comments.serializers import CommentsSerializer
from apps.orders.models import OrdersModel
from apps.orders.serializers import OrderSerializer
from drf_yasg.utils import swagger_auto_schema


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
        order.refresh_from_db()
        comment_serializer = OrderSerializer(order)
        return Response(comment_serializer.data, status.HTTP_201_CREATED)
