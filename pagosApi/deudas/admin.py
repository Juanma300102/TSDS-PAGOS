from django.contrib import admin
from deudas.models import Deuda


class DeudaAdmin(admin.ModelAdmin):
    ...


admin.site.register(Deuda, DeudaAdmin)
