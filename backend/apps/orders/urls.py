from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import GeneralOrdersStatisticsView, OrderViewSet, UpdateOrderView

router = DefaultRouter()
router.register(r'list', OrderViewSet, basename='list_export_orders')

urlpatterns = [
    path('/', include(router.urls)),
    path('/general_statistic', GeneralOrdersStatisticsView.as_view(), name='general_statistic'),
    path('/<int:order_pk>/group/<int:group_pk>', UpdateOrderView.as_view(), name='update_order'),
]
