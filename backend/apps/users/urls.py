from django.urls import path

from .views import GetMeView, ListCreateManagerView, ManagerBanView, ManagerUnbanView

urlpatterns = [
    path('/managers', ListCreateManagerView.as_view(), name='register_manager'),
    path('/managers/<int:pk>/ban', ManagerBanView.as_view(), name='manager_ban'),
    path('/managers/<int:pk>/unban', ManagerUnbanView.as_view(), name='manager_unban'),
    path('/managers/info', GetMeView.as_view(), name='manager_info'),

]