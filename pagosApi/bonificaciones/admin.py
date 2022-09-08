from django.contrib import admin
from bonificaciones.models import Bonificacion


class BonificacionAdmin(admin.ModelAdmin):
    ...


admin.site.register(Bonificacion, BonificacionAdmin)
