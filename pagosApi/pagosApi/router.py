from django.urls import include, path

urlpatterns = [path("", include(("conceptos.url", "conceptos"), "conceptos"))]
