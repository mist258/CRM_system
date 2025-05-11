from django.urls import path

from .views import CreateListGroupView, RetrieveGroupView

urlpatterns = [
    path('/create_list_groups', CreateListGroupView.as_view(), name='create_list_group'),
    path('/<int:pk>/get_group', RetrieveGroupView.as_view(), name='get_group'),

]
