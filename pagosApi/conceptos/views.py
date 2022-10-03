from rest_framework.generics import mixins
from rest_framework.viewsets import ModelViewSet
from conceptos.serializers import ConceptoSerializer, Concepto


class ConceptoViewSet(ModelViewSet):
    queryset = Concepto.objects.all()
    serializer_class = ConceptoSerializer


# Create your views here.
