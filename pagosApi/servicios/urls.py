from rest_framework.routers import SimpleRouter
from servicios.views import ServiciosViewSet

router = SimpleRouter()
router.register("servicios", ServiciosViewSet)

urlpatterns = router.urls
