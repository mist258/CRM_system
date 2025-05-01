from django.urls import path

from .views import AssignedOrderToManager, CommentOrderCreateView, GetMyOrdersView, OrderListView

urlpatterns = [
    path('/listing', OrderListView.as_view(), name='order_listing'),
    path('/manager_list', GetMyOrdersView.as_view(), name='get_my_orders'),
    path('/<int:pk>/comments', CommentOrderCreateView.as_view(), name='comment'),
    path('/<int:pk>/assign_order', AssignedOrderToManager.as_view(), name='assign_order'),

]