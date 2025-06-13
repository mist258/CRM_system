from django.urls import path

from .views import GeneralOrdersStatisticsView, OrderListView, UpdateOrderView

urlpatterns = [
    path('', OrderListView.as_view(), name='order_listing'),
    path('/general_statistic', GeneralOrdersStatisticsView.as_view(), name='general_statistic'),
    path('/<int:order_pk>/group/<int:group_pk>', UpdateOrderView.as_view(), name='update_order'),
]