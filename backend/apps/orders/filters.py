from django_filters import rest_framework as filters

from .choices.application_choices import CoursesChoices, FormatCourseChoices, StatusChoices, TypeCourseChoices
from .models import OrdersModel


class OrderFilter(filters.FilterSet):

    # search by incomplete pattern
    name = filters.CharFilter('name', 'icontains')
    surname = filters.CharFilter('surname', 'icontains')
    email = filters.CharFilter('email', 'icontains')
    phone = filters.CharFilter('phone', 'icontains')

    # search in range
    sum_range = filters.RangeFilter(field_name='sum')
    alreadyPaid_range = filters.RangeFilter(field_name='alreadyPaid')
    age_range = filters.RangeFilter(field_name='age')
    created_at = filters.DateFromToRangeFilter(field_name='created_at')

    # search in choices
    course = filters.ChoiceFilter('course', choices=CoursesChoices)
    course_type = filters.ChoiceFilter('course_type', choices=TypeCourseChoices)
    status = filters.ChoiceFilter('status', choices=StatusChoices )
    course_format = filters.ChoiceFilter('course_format', choices=FormatCourseChoices)

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
