from django_filters import rest_framework as filters

from .choices.application_choices import CoursesChoices, FormatCourseChoices, StatusChoices, TypeCourseChoices
from .models import OrdersModel


class OrderFilter(filters.FilterSet):

    sum_range = filters.RangeFilter(field_name='sum')
    alreadyPaid_range = filters.RangeFilter(field_name='alreadyPaid')
    age_range = filters.RangeFilter(field_name='age')
    course = filters.ChoiceFilter(field_name='course', choices=CoursesChoices)
    course_type = filters.ChoiceFilter(field_name='course_type', choices=TypeCourseChoices)
    status = filters.ChoiceFilter(field_name='status', choices=StatusChoices )
    course_format = filters.ChoiceFilter(field_name='course_format', choices=FormatCourseChoices)

    class Meta:
        model = OrdersModel
        fields = ['id', 'name', 'surname',
                'email', 'phone', 'age',
                'course', 'course_format', 'course_type',
                'status', 'sum', 'alreadyPaid',
                'created_at',]
