from dataclasses import field
from servicios.models import Servicio
from rest_framework.serializers import ModelSerializer


class ServiciosSerializer(ModelSerializer):
    class meta:
        model = Servicio
        field = "__all__"
