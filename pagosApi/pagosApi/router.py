from unittest.mock import patch
from django.urls import include, path

urlpatterns = [
    path("", include(("conceptos.url", "conceptos"), "conceptos")),
    path("", include(("bonificaciones.urls", "bonificaciones"), "bonificaciones")),
    path("", include(("deudas.urls", "deudas"), "deudas")),
    path("", include(("personas.urls", "personas"), "personas")),
    path("", include(("periodos.urls", "periodos"), "periodos")),
    path("", include(("servicios.urls", "servicios"), "servicios")),
    path("", include(("montosBase.urls", "montosBase"), "montosBase")),
    patch("", include(("pagosADeudas.urls", "pagosADeudas"), "pagosADeudas")),
    patch("", include(("pagosUnicos.urls", "pagosUnicos"), "pagosUnicos")),
    path("", include(("pagosADeudas.urls", "pagosADeudas"), "pagosADeudas")),
    path("", include(("recargos.urls", "recargos"), "recargos")),
]
