from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import serializers

from core.services.email_service import EmailService

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
        EmailService.activate(user)
        return user


