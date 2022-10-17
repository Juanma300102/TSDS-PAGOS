from rest_framework.viewsets import ModelViewSet
from deudas.serializers import DeudaSerializer, Deuda


class DeudaViewSet(ModelViewSet):
    queryset = Deuda.objects.all()
    serializer_class = DeudaSerializer
