from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.comments.serializers import CommentsSerializer
from apps.groups.serializers import GroupSerializer
from apps.users.serializers import UserSerializer

from .models import OrdersModel

UserModel = get_user_model()


class OrderSerializer(serializers.ModelSerializer):
    manager = UserSerializer(read_only=True)
    comments = CommentsSerializer(read_only=True, many=True)
    group = GroupSerializer(read_only=True)

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
                  'comments',
                  'group',
                  'alreadyPaid',
                  'created_at',
                  )
        read_only_fields = ('id',
                            'created_at',
                            'manager',
                            'group',
                            'comments',
                            )

        extra_kwargs = {
            'group': {
                'required': True
            },
        }


