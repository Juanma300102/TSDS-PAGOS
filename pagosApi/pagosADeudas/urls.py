from rest_framework.routers import SimpleRouter
from pagosADeudas.views import PagosADeudasViewSet

router = SimpleRouter()
router.register("pagos-a-deudas", PagosADeudasViewSet)

urlpatterns = router.urls
