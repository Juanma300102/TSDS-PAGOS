from rest_framework import routers
from conceptos.views import ConceptoViewSet


conceptos_router = routers.SimpleRouter()
conceptos_router.register("conceptos", ConceptoViewSet)

urlpatterns = conceptos_router.urls
