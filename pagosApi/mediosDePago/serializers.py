from dataclasses import fields
from mediosDePago.models import Mediosdepago
from rest_framework.serializers import ModelSerializer


class MediosDePagoSerializer(ModelSerializer):
    class Meta:
        model = Mediosdepago
        fields = "__all__"
