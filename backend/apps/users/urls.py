from django.urls import path

from .views import GetMeView, ListCreateManagerView, ManagerBanView, ManagerUnbanView

urlpatterns = [
    path('/register/manager', ListCreateManagerView.as_view(), name='register_manager'),
    path('/manager/<int:pk>/ban', ManagerBanView.as_view(), name='manager_ban'),
    path('/manager/<int:pk>/unban', ManagerUnbanView.as_view(), name='manager_unban'),
    path('/manager/info', GetMeView.as_view(), name='manager_info'), # add readme

]