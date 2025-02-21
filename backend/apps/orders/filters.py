from django_filters import rest_framework as filters

from .models import OrdersModel


class OrderFilter(filters.FilterSet):
    class Meta:
        model = OrdersModel
        fields = ['id', 'name', 'surname',
                'email', 'phone', 'age',
                'course', 'course_format', 'course_type',
                'status', 'sum', 'alreadyPaid',
                'created_at',]

