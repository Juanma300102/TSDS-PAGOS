from servicios.models import Servicio
from rest_framework.serializers import ModelSerializer


class ServiciosSerializer(ModelSerializer):
    class Meta:
        model = Servicio
        fields = "__all__"
