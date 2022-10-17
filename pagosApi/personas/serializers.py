from dataclasses import fields
from personas.models import Persona
from rest_framework.serializers import ModelSerializer


class PersonasSerializer(ModelSerializer):
    class Meta:
        model = Persona
        fields = "__all__"
