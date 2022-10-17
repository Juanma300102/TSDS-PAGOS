from rest_framework.viewsets import ModelViewSet
from servicios.serializers import ServiciosSerializer, Servicio


class ServiciosViewSet(ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServiciosSerializer
