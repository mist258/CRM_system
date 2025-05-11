from django.urls import path

from .views import (
    GeneralOrdersStatisticsView,
    GetMyOrdersView,
    OrderListView,
    OrderStatisticsByManagerView,
    UpdateOrderView,
)

urlpatterns = [
    path('', OrderListView.as_view(), name='order_listing'),
    path('/manager_list', GetMyOrdersView.as_view(), name='get_my_orders'),
    path('/general_statistic', GeneralOrdersStatisticsView.as_view(), name='general_statistic'),
    path('/manager_statistic', OrderStatisticsByManagerView.as_view(), name='manager_statistic'),
    path('/<int:order_pk>/group/<int:group_pk>', UpdateOrderView.as_view(), name='update_order'),
]