from montosBase.views import MontoBaseModelViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register("montos-base", MontoBaseModelViewSet)

urlpatterns = router.urls
