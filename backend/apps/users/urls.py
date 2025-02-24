from django.urls import path

from .views import ListCreateManagerView

urlpatterns = [
    path('/register/manager', ListCreateManagerView.as_view(), name='register-manager'),

]