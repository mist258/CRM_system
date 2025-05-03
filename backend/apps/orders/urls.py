from django.urls import path

from .views import (
    AssignedOrderToManager,
    CommentOrderCreateView,
    GeneralOrdersStatisticsView,
    GetMyOrdersView,
    OrderListView,
)

urlpatterns = [
    path('/listing', OrderListView.as_view(), name='order_listing'),
    path('/manager_list', GetMyOrdersView.as_view(), name='get_my_orders'),
    path('/<int:pk>/assign_order', AssignedOrderToManager.as_view(), name='assign_order'),
    path('/<int:pk>/comments', CommentOrderCreateView.as_view(), name='comment'),
    path('/general_statistic', GeneralOrdersStatisticsView.as_view(), name='general_statistic'),

]