from unittest.mock import patch
from django.urls import include, path

urlpatterns = [
    path("", include(("conceptos.url", "conceptos"), "conceptos")),
    path("", include(("bonificaciones.urls", "bonificaciones"), "bonificaciones")),
    path("", include(("periodos.url", "periodos"), "periodos")),
    path("", include(("servicios.urls", "servicios"), "servicios")),
    path("", include(("montosBase.urls", "montosBase"), "montosBase")),
    patch("", include(("pagosADeudas.urls", "pagosADeudas"), "pagosADeudas")),
]
