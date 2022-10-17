from rest_framework.viewsets import ModelViewSet
from pagosUnicos.serializers import PagosUnicosSerializer, PagoUnico


class PagosUnicosViewSet(ModelViewSet):
    queryset = PagoUnico.objects.all()
    serializer_class = PagosUnicosSerializer
