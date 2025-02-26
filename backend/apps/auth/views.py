from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.users.serializers import UserSerializer
from core.services.email_service import ActivateToken, EmailService
from core.services.jwt_service import JWTService
from drf_yasg.utils import swagger_auto_schema

UserModel = get_user_model()
@method_decorator(name='post', decorator=swagger_auto_schema(operation_id='send activation token',
                                                             responses={200: UserSerializer()}))
class SendActivationEmailView(GenericAPIView):
    '''
        sen email with activation token
    '''
    serializer_class = UserSerializer
    
    def post(self, *args, **kwargs):
        user = self.get_object()
        EmailService.activate(user)
        return Response({"Details" : "Email was sent to user "},
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

