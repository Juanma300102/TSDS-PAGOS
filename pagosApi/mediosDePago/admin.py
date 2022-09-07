from django.contrib import admin

from mediosDePago.models import MedioDePago


class MedioDePagoAdmin(admin.ModelAdmin):
    ...


admin.site.register(MedioDePago, MedioDePagoAdmin)
