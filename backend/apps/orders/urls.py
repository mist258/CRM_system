from django.urls import path

from .views import (
    AssignedOrderToManager,
    CommentOrderCreateView,
    CreateListGroupView,
    GeneralOrdersStatisticsView,
    GetMyOrdersView,
    OrderListView,
    OrderStatisticsByManagerView,
    RetrieveGroupView,
    UpdateOrderView,
)

urlpatterns = [
    path('/listing', OrderListView.as_view(), name='order_listing'),
    path('/manager_list', GetMyOrdersView.as_view(), name='get_my_orders'),
    path('/<int:pk>/assign_order', AssignedOrderToManager.as_view(), name='assign_order'),
    path('/<int:pk>/comments', CommentOrderCreateView.as_view(), name='comment'),
    path('/general_statistic', GeneralOrdersStatisticsView.as_view(), name='general_statistic'),
    path('/manager_statistic', OrderStatisticsByManagerView.as_view(), name='manager_statistic'),
    path('/create_list_groups', CreateListGroupView.as_view(), name='create_list_group'),
    path('/<int:order_pk>/group/<int:group_pk>', UpdateOrderView.as_view(), name='update_order'),
    path('/<int:pk>/get_group', RetrieveGroupView.as_view(), name='get_group'),
]