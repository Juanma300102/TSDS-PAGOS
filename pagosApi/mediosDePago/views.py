from rest_framework.viewsets import ModelViewSet
from mediosDePago.models import MedioDePago
from mediosDePago.serialiserzs import MediosDePagoSerializer, MediosDePago


class BonificacionesViewSet(ModelViewSet):
    queryset = MedioDePago.objects.all()
    serializer_class = MediosDePagoSerializer
