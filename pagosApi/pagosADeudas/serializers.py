from pagosADeudas.models import PagoADeuda
from rest_framework.serializers import ModelSerializer


class PagosADeudasSerializer(ModelSerializer):
    class Meta:
        model = PagoADeuda
        fields = "__all__"
