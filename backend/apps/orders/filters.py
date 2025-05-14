from django_filters import rest_framework as filters

from .choices.application_choices import CoursesChoices, FormatCourseChoices, StatusChoices, TypeCourseChoices
from .models import OrdersModel


class OrderFilter(filters.FilterSet):

    # search by incomplete pattern
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    surname = filters.CharFilter(field_name='surname', lookup_expr='icontains')
    email = filters.CharFilter(field_name='email', lookup_expr='icontains')
    phone = filters.CharFilter(field_name='phone', lookup_expr='icontains')

    # search in range
    sum_range = filters.RangeFilter(field_name='sum')
    alreadyPaid_range = filters.RangeFilter(field_name='alreadyPaid')
    age_range = filters.RangeFilter(field_name='age')

    # search in choices
    course = filters.ChoiceFilter(field_name='course', choices=CoursesChoices)
    course_type = filters.ChoiceFilter(field_name='course_type', choices=TypeCourseChoices)
    status = filters.ChoiceFilter(field_name='status', choices=StatusChoices )
    course_format = filters.ChoiceFilter(field_name='course_format', choices=FormatCourseChoices)

    # shows the manager his own requests
    own_orders = filters.BooleanFilter(method='filter_own_orders')

    def filter_own_orders(self, queryset, name, value):
        if value and self.request and self.request.user.is_authenticated:
            return queryset.filter(manager=self.request.user)
        return queryset

    class Meta:
        model = OrdersModel
        fields = ['id', 'name', 'surname',
                'email', 'phone', 'age',
                'course', 'course_format', 'course_type',
                'status', 'sum', 'alreadyPaid',
                'created_at',]
