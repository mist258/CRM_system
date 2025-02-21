from django_filters import rest_framework as filters


class OrderFilter(filters.FilterSet):
    ordering = filters.OrderingFilter(
        fields=('id',
                'name',
                'surname',
                'email',
                'phone',
                'age',
                'course',
                'course_format',
                'course_type',
                'status',
                'sum',
                'alreadyPaid',
                'created_at',
                )
    )