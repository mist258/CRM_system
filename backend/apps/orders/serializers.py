from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.users.serializers import UserSerializer

from .models import OrdersModel

UserModel = get_user_model()

# class CommentsModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CommentsModel
#         fields = ('id',
#                   'text')


class OrderSerializer(serializers.ModelSerializer):
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

class AssignOrderToManagerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ('id',
                  'email',
                  'name',
                  'surname',
                  'orders')