from django.contrib import admin
from suscripciones.models import Suscripcion


class SuscripcionAdmin(admin.ModelAdmin):
    ...


admin.site.register(Suscripcion, SuscripcionAdmin)
