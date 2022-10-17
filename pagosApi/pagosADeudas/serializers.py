from dataclasses import field
from pagosADeudas.models import PagoADeuda
from rest_framework.serializers import ModelSerializer


class PagosADeudasSerializer(ModelSerializer):
    class meta:
        model = PagoADeuda
        field = "__all__"
