import re

from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

UserModel = get_user_model()

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class SetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField() # maybe write_only=True

    def validate(self, attrs):

        password = attrs.get("password")

        pattern = r"^[A-Za-z\d@$!%*?&]{8,}$"

        if not re.fullmatch(pattern, password):
            raise ValidationError('Password must contain at least 8 characters, '
                                  '1 special symbol, 1 letter, 1 number')
        return attrs
