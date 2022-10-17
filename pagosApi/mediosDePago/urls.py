from rest_framework.routers import SimpleRouter
from mediosDePago.views import MediosDePagoViewSet

router = SimpleRouter()
router.register("medios-de-pago", MediosDePagoViewSet)

urlpatterns = router.urls
