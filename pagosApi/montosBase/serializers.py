import imp
from montosBase.models import MontoBase
from rest_framework.serializers import ModelSerializer


class MontoBaseModelSerializer(ModelSerializer):
    class Meta:
        model = MontoBase
        fields = "__all__"
