from rest_framework.serializers import ModelSerializer
from conceptos.models import Concepto


class ConceptoSerializer(ModelSerializer):
    class Meta:
        model = Concepto
        fields = "__all__"
