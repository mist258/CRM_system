from rest_framework import serializers

from apps.users.serializers import UserSerializer

from .models import OrdersModel

# class CommentsModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CommentsModel
#         fields = ('id',
#                   'text')


class OrderSerializer(serializers.ModelSerializer):  # in work
    manager = UserSerializer(read_only=True)

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
                  'manager',
                  'alreadyPaid',
                  'created_at',                  )
        read_only_fields = ('id',
                            'created_at',
                            )
