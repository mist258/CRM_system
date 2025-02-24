from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView

from .serializers import UserSerializer

UserModel = get_user_model()

class ListCreateManagerView(ListCreateAPIView):
    '''
        create & list a new manager
        (allowed superuser only)
    '''
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

