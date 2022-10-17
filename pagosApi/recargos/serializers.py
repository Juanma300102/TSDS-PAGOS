from dataclasses import fields
from recargos.models import Recargo
from rest_framework.serializers import ModelSerializer


class RecargosSerializer(ModelSerializer):
    class Meta:
        model = Recargo
        fields = "__all__"
