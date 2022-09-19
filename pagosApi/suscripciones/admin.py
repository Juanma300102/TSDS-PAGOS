from django.contrib import admin
from suscripciones.models import suscripcion


class SuscripcionAdmin(admin.ModelAdmin):
    ...


admin.site.register(suscripcion, SuscripcionAdmin)
