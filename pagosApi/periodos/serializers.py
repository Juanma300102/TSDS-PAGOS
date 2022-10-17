from dataclasses import fields
from periodos.models import Periodo
from rest_framework.serializers import ModelSerializer


class PeriodosSerializer(ModelSerializer):
    class Meta:
        model = Periodo
        fields = "__all__"
