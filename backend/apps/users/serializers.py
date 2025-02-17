from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import UserProfileModel

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = ('id',
                  'name',
                  'surname',
                  'user',
                  'created_at',
                  'updated_at',
                  )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = UserModel
        fields = ('id',
                  'email',
                  'is_active',
                  'is_staff',
                  'is_superuser',
                  'last_login',
                  'created_at',
                  'updated_at',
                  'profile',
                  )

        read_only_fields = ('id',
                            'is_active',
                            'is_staff',
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
