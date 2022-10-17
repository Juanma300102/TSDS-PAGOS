from rest_framework.routers import SimpleRouter
from periodos.views import PeriodosViewSet

router = SimpleRouter()
router.register("periodos", PeriodosViewSet)

urlpatterns = router.urls
