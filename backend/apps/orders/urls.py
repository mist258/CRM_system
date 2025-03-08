from django.urls import path

from .views import CommentOrderCreateView, GetMyOrdersView, OrderListView

urlpatterns = [
    path('/listing', OrderListView.as_view(), name='order_listing'),
    path('/manager_list', GetMyOrdersView.as_view(), name='get_my_orders'),
    path('/comment', CommentOrderCreateView.as_view(), name='comment'),

]