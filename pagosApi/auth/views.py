from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from auth.serializers import AuthSerializer
from django.contrib.auth import login
from django.contrib.auth.models import User


class AuthViewSet(GenericViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ("login"):
            return AuthSerializer

    @action(methods=["POST"], detail=False)
    def login(self, request, *args, **kwargs):
        serializer: AuthSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user", None)
        if not user:
            raise ValidationError(
                "Something went wrong and there is no user in the view"
            )
        login(request, user)
        return Response(status=status.HTTP_202_ACCEPTED)
