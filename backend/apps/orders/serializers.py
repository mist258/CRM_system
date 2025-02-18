from rest_framework import serializers

from .models import OrdersModel


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersModel
        fields = ('id',
                  'email',
                  'name',
                  'surname',
                  'phone',
                  'age',
                  'course',
                  'course_type',
                  'course_format',
                  'status',
                  'sum',
                  'alreadyPaid',
                  'created_at',                  )
        read_only_fields = ('id',
                            'created_at',
                            )
