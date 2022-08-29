from django.contrib import admin
from montosBase.models import MontoBase

# Register your models here.
class MontosBaseAdmin(admin.ModelAdmin):
    ...


admin.site.register(MontoBase, MontosBaseAdmin)
