from django.contrib import admin
from recargos.models import Recargo


class RecargoAdmin(admin.ModelAdmin):
    ...


admin.site.register(Recargo, RecargoAdmin)