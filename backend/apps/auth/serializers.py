import re

from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.exceptions.password_exception import PasswordException

UserModel = get_user_model()

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class SetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):

        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        pattern = r"^[A-Za-z\d@$!%*?&]{8,}$"

        if not re.fullmatch(pattern, password):
            raise ValidationError('Password must contain at least 8 characters, '
                                  '1 special symbol, 1 letter, 1 number')

        if password != confirm_password:
            raise PasswordException

        return attrs
