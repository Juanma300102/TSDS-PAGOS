from rest_framework.viewsets import ModelViewSet
from recargos.serializers import RecargosSerializer, Recargo


class RecargosViewSet(ModelViewSet):
    queryset = Recargo.objects.all()
    serializer_class = RecargosSerializer


# Create your views here.
