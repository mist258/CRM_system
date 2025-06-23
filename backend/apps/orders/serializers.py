from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.comments.serializers import CommentsSerializer
from apps.groups.serializers import GroupSerializer
from apps.users.serializers import UserSerializer

from ..groups.models import GroupModel
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

    def update(self, instance, validated_data):

        group_name = self.initial_data.get('group')
        request = self.context.get('request')
        user = request.user

        if group_name:
            try:
                group = GroupModel.objects.get(name=group_name)
                instance.group = group
            except GroupModel.DoesNotExist:
                raise ValidationError({"detail" : "This group name does not exist" })

        new_status = validated_data.get('status', instance.status)

        if instance.manager is None and user is not None:
            instance.manager = user
            instance.status = new_status

        if new_status == "New":
            instance.status = new_status
            instance.manager = None

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

