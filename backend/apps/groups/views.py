from django.utils.decorators import method_decorator

from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from .models import GroupModel
from .serializers import GroupSerializer


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
