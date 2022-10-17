from montosBase.serializers import MontoBase, MontoBaseModelSerializer
from rest_framework.viewsets import ModelViewSet


class MontoBaseModelViewSet(ModelViewSet):
    queryset = MontoBase.objects.all()
    serializer_class = MontoBaseModelSerializer
