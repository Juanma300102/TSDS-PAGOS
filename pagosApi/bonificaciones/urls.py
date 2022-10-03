from rest_framework.routers import SimpleRouter
from bonificaciones.views import BonificacionesViewSet

router = SimpleRouter()
router.register("bonificaciones", BonificacionesViewSet)

urlpatterns = router.urls
