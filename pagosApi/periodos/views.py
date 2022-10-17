from rest_framework.viewsets import ModelViewSet
from periodos.serializers import PeriodosSerializer, Periodo


class PeriodosViewSet(ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodosSerializer


# Create your views here.
