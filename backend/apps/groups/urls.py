from django.urls import path

from .views import CreateListGroupView, RetrieveGroupView

urlpatterns = [
    path('', CreateListGroupView.as_view(), name='create_list_group'),
    path('/<int:pk>', RetrieveGroupView.as_view(), name='get_group'),

]
