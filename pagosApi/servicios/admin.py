from django.contrib import admin
from servicios.models import Servicio


class ServicioAdmin(admin.ModelAdmin):
    ...


admin.site.register(Servicio, ServicioAdmin)
