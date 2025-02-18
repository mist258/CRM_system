from django.urls import path

from .views import OrderListView

urlpatterns = [
    path('/listing', OrderListView.as_view(), name='order_listing'),

]