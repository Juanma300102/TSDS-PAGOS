from django.contrib import admin
from pagosUnicos.models import PagoUnico


class PagoUnicoAdmin(admin.ModelAdmin):
    ...


admin.site.register(PagoUnico, PagoUnicoAdmin)
