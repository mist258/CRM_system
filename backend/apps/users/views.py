from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.permissions.is_superuser_permission import IsSuperUser
from drf_yasg.utils import swagger_auto_schema

from .serializers import ManagerStatisticsSerializer, UserSerializer

UserModel = get_user_model()


@method_decorator(name='post', decorator=swagger_auto_schema(operation_id='create manager',
                                                             responses={200: UserSerializer()}))
@method_decorator(name= 'get',decorator=swagger_auto_schema(operation_id='show all managers',
                                                            responses={200: UserSerializer()}))
class ListCreateManagerView(generics.ListCreateAPIView):
    '''
    get:
        list all managers
        (allowed superuser only)
    post:
        create a new manager

    '''
    queryset = UserModel.objects.select_related('profile').all()
    permission_classes = (IsSuperUser,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ManagerStatisticsSerializer
        return UserSerializer


@method_decorator(name='patch', decorator=swagger_auto_schema(operation_id = 'ban manager by id',
                                                            responses={200: UserSerializer()}))
class ManagerBanView(generics.GenericAPIView):
    '''
         ban a manager
         (allowed superuser only)
    '''
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        return UserModel.objects.select_related('profile').exclude(pk = self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_active and not user.is_blocked:
            user.is_active = False
            user.is_blocked = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

@method_decorator(name='patch', decorator=swagger_auto_schema(operation_id='unban manager by id',
                                                            responses={200: UserSerializer()}))
class ManagerUnbanView(generics.GenericAPIView):
    '''
         unban a manager
         (allowed superuser only)
    '''
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        return UserModel.objects.select_related('profile').exclude(pk = self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_active and user.is_blocked:
            user.is_active = True
            user.is_blocked = False
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='show me',
                                                            responses={200: UserSerializer()}))
class GetMeView(generics.GenericAPIView):
    '''
        get my info
    '''
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

