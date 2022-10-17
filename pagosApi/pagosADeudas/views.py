from rest_framework.viewsets import ModelViewSet
from pagosADeudas.serializers import PagosADeudasSerializer, PagoADeuda


class PagosADeudasViewSet(ModelViewSet):
    queryset = PagoADeuda.objects.all()
    serializer_class = PagosADeudasSerializer
