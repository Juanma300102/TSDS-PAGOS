from rest_framework.viewsets import ModelViewSet
from personas.serializers import PersonasSerializer, Persona


class PersonasViewSet(ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonasSerializer
