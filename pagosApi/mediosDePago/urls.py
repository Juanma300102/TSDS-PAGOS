from rest_framework.routers import SimpleRouter
from mediosDePago.views import MediosDePagoViewSet

router = SimpleRouter()
router.register("mediosdepago", MediosDePagoViewSet)

urlpatterns = router.urls
