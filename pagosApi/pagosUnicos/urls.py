from rest_framework.routers import SimpleRouter
from pagosUnicos.views import PagosUnicosViewSet

router = SimpleRouter()
router.register("pagosUnicos", PagosUnicosViewSet)

urlpatterns = router.urls
