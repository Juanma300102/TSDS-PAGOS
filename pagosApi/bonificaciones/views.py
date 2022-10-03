from rest_framework.viewsets import ModelViewSet
from bonificaciones.serializers import BonificacionesSerializer, Bonificacion


class BonificacionesViewSet(ModelViewSet):
    queryset = Bonificacion.objects.all()
    serializer_class = BonificacionesSerializer
