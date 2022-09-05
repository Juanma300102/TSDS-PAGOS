from django.contrib import admin
from periodos.models import Periodo


class PeriodoAdmin(admin.ModelAdmin):
    ...


admin.site.register(Periodo, PeriodoAdmin)
