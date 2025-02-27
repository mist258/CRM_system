from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from rest_framework import generics, status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response

from apps.users.serializers import UserSerializer
from core.services.email_service import ActivateToken, EmailService
from core.services.jwt_service import JWTService, RecoveryToken
from drf_yasg.utils import swagger_auto_schema

from .serializers import EmailSerializer, PasswordSerializer

UserModel = get_user_model()
@method_decorator(name='post', decorator=swagger_auto_schema(operation_id='send activation token',
                                                             responses={200: UserSerializer()}))
class SendActivationEmailView(GenericAPIView):
    '''
        sen email with activation token
    '''
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    
    def post(self, *args, **kwargs):
        user = self.get_object()
        EmailService.activate(user)
        return Response({"Details" : "Email was sent to user"},
                        status=status.HTTP_200_OK)


@method_decorator(name='patch', decorator=swagger_auto_schema(operation_id='activate manager',
                                                              responses={200: UserSerializer()}))
class ActivationManagerView(generics.GenericAPIView):
    '''
        send mail for activation
    '''
    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.verify_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ConfirmationPasswordView(generics.GenericAPIView):
    '''
        confirm user's password
    '''

    def post(self, request, *args, **kwargs):
        data = request.data
        #todo



class RecoveryPasswordRequestView(generics.GenericAPIView):
    '''
        request to recover password
    '''
    serializer_class = EmailSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, **serializer.data)
        EmailService.recovery_password(user)
        return Response({"Details" : "Email was sent to user"},)

class RecoveryPasswordView(generics.GenericAPIView):
    '''
        recover password
    '''
    serializer_class = PasswordSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = kwargs['token']
        user = JWTService.verify_token(token, RecoveryToken)
        user.set_password(serializer.data['password'])
        user.save()
        return Response({"Details" : "Password has been changed."},
                        status=status.HTTP_200_OK)







