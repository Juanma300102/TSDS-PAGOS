from rest_framework.routers import SimpleRouter
from personas.views import PersonasViewSet

router = SimpleRouter()
router.register("personas", PersonasViewSet)

urlpatterns = router.urls
