from django.contrib.auth import get_user_model

from rest_framework import serializers

UserModel = get_user_model()

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    

class SetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField(write_only=True)
