from dataclasses import field
from pagosUnicos.models import PagoUnico
from rest_framework.serializers import ModelSerializer


class PagosUnicosSerializer(ModelSerializer):
    class meta:
        model = PagoUnico
        field = "__all__"
