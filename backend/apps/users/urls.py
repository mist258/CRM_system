from django.urls import path

from .views import ListCreateManagerView, ManagerBanView, ManagerUnbanView

urlpatterns = [
    path('/register/manager', ListCreateManagerView.as_view(), name='register-manager'),
    path('/manager/<int:pk>/ban', ManagerBanView.as_view(), name='manager-ban'),
    path('/manager/<int:pk>/unban', ManagerUnbanView.as_view(), name='manager-unban'),

]