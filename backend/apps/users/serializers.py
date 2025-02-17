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