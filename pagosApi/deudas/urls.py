from rest_framework.routers import SimpleRouter
from deudas.views import DeudaViewSet

router = SimpleRouter()
router.register("deudas", DeudaViewSet)

urlpatterns = router.urls
