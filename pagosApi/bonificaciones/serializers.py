from dataclasses import fields
from bonificaciones.models import Bonificacion
from rest_framework.serializers import ModelSerializer


class BonificacionesSerializer(ModelSerializer):
    class Meta:
        model = Bonificacion
        fields = "__all__"
