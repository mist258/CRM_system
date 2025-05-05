from django.contrib.auth import get_user_model
from django.db.models import Count

from rest_framework import serializers

from apps.users.serializers import ProfileSerializer, UserSerializer

from .models import CommentsModel, GroupModel, OrdersModel

UserModel = get_user_model()


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentsModel
        fields = ('id',
                  'text',
                  'order',
                  )

        read_only_fields = ('id',
                            'created_at',
                            'order',
                            )

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupModel
        fields = ('id',
                  'name',
                  )


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


class AssignOrderToManagerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)
    name = serializers.CharField(source='profile.name', read_only=True)
    surname = serializers.CharField(source='profile.surname', read_only=True)

    class Meta:
        model = UserModel
        fields = ('id',
                  'email',
                  'name',
                  'surname',
                  'orders',
                  )


class ManagerStatisticsSerializer(serializers.ModelSerializer):
    order_statistics = serializers.SerializerMethodField()
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = UserModel
        fields = ('id',
                  'email',
                  'profile',
                  'order_statistics',
                  )

    def get_order_statistics(self, obj):
        orders = OrdersModel.objects.filter(manager=obj)

        status_count = orders.values('status').annotate(total=Count('status'))

        statistics = {}

        for item in status_count:
            status_name = item['status']
            statistics[status_name] = item['total']

        return {
            'total_orders': orders.count(),
            'by_status': statistics
        }
