from django.contrib.auth import get_user_model
from django.db.models import Count
from django.db.transaction import atomic

from rest_framework import serializers

from apps.orders.models import OrdersModel

from .models import UserProfileModel

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = ('id',
                  'name',
                  'surname',
                  'created_at',
                  'updated_at',
                  )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = ('id',
                  'email',
                  'is_active',
                  'is_staff',
                  'is_blocked',
                  'is_superuser',
                  'last_login',
                  'profile',
                  )

        read_only_fields = ('id',
                            'is_active',
                            'is_staff',
                            'is_blocked',
                            'is_superuser',
                            'last_login',
                            'created_at',
                            'updated_at',
                            )

        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

    @atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_manager(**validated_data)
        UserProfileModel.objects.create(user=user, **profile)
        return user


class ManagerStatisticsSerializer(serializers.ModelSerializer):
    order_statistics = serializers.SerializerMethodField()
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = UserModel
        fields = ('id',
                  'email',
                  'profile',
                  'is_active',
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

