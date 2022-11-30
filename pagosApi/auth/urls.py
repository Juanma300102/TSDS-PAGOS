from rest_framework import routers
from auth.views import AuthViewSet


auth_router = routers.SimpleRouter()
auth_router.register("auth", AuthViewSet)

urlpatterns = auth_router.urls
