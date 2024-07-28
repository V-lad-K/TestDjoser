import re

from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", 'username', 'email', 'password']

    @staticmethod
    def validate_username(value):
        regex_username_pattern = "^[A-Za-z0-9_]*$"

        if not len(value):
            raise serializers.ValidationError("Username must be not empty")
        if " " in value:
            raise serializers.ValidationError("Username must not contain spaces")
        if not (5 <= len(value) <= 150):
            raise serializers.ValidationError("Username must be in range 5 - 150")
        if not re.match(regex_username_pattern, value):
            raise serializers.ValidationError("Username should contain only latin letters, numbers, underscores")
        if all([char.isdigit() for char in value]):
            raise serializers.ValidationError("Username should not contain only numbers")

        return value

    @staticmethod
    def validate_email(value):
        regex_email_pattern = r"^[A-Za-z0-9]+([._-][A-Za-z0-9]+)*@[A-Za-z0-9]+([._-][A-Za-z0-9]+)*$"

        if not len(value):
            raise serializers.ValidationError("Email must be not empty")
        if " " in value:
            raise serializers.ValidationError("Email must not contain spaces")
        if not 15 <= len(value) <= 150:
            raise serializers.ValidationError("Email must be in range 10 - 150")
        if len(value.split("@")[0]) < 5:
            raise serializers.ValidationError("Local part of email must be more than 5 characters")
        if len(value.split("@")[1]) < 3:
            raise serializers.ValidationError("Domain part of email must be more than 5 characters")
        if not re.match("^[A-Za-z0-9]*$", value[0]):
            raise serializers.ValidationError("First letter of email must be a letter")
        if not re.match(regex_email_pattern, value):
            raise serializers.ValidationError(
                """Email should contain only latin letters, numbers, underscores,
                 periods, or dashes and must follow the correct format""")

        return value

    @staticmethod
    def validate_password(value):
        regex_password_pattern = "^[^\u0400-\u04FF]*$"

        if " " in value:
            raise serializers.ValidationError("Password must not contain spaces")
        if not 8 <= len(value) <= 150:
            raise serializers.ValidationError("Password must be in range 8 - 150")
        if not any([char.isupper() for char in value]):
            raise serializers.ValidationError("Password must have at least 1 upper character")
        if not any([char.isdigit() for char in value]):
            raise serializers.ValidationError("Password must have at least 1 digit")
        if not re.match(regex_password_pattern, value):
            raise serializers.ValidationError("The password must not contain Cyrillic characters")

        return value
