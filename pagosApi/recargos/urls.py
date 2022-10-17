from rest_framework.routers import SimpleRouter
from recargos.views import RecargosViewSet

router = SimpleRouter()
router.register("recargos", RecargosViewSet)

urlpatterns = router.urls
