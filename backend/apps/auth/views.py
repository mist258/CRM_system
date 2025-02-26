from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.response import Response

from apps.users.serializers import UserSerializer

UserModel = get_user_model()

class ActivationManagerView(generics.GenericAPIView):
    '''
        send mail for activation
    '''
    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        pass
