from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from deudas.models import Deuda


class DeudaSerializer(ModelSerializer):
    class Meta:
        model = Deuda
        fields = "__all__"
