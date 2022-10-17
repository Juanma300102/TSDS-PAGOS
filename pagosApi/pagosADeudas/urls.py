from rest_framework.routers import SimpleRouter
from pagosADeudas.views import PagosADeudasViewSet

router = SimpleRouter()
router.register("servicios", PagosADeudasViewSet)

urlpatterns = router.urls
