from rest_framework import serializers, exceptions
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_password(self, value):
        if not value:
            raise exceptions.ValidationError("You must provide a password")
        return value

    def validate_username(self, value):
        if not value:
            raise exceptions.ValidationError("You must provide am username")
        return value

    def validate(self, attrs: dict):
        user = authenticate(self.context.get("request"))
        if not user:
            raise exceptions.AuthenticationFailed("Invalid credentials")
        attrs.setdefault("user", user)
        return super().validate(attrs)
