from django.contrib import admin
from pagosADeudas.models import PagoADeuda


class PagoADeudaAdmin(admin.ModelAdmin):
    ...


admin.site.register(PagoADeuda, PagoADeudaAdmin)
