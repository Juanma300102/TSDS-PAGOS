from django.urls import include, path

urlpatterns = [
    path("", include(("conceptos.url", "conceptos"), "conceptos")),
    path("", include(("bonificaciones.urls", "bonificaciones"), "bonificaciones")),
]
