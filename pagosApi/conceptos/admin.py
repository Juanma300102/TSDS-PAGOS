from django.contrib import admin
from conceptos.models import Concepto


class ConceptoAdmin(admin.ModelAdmin):
    ...


admin.site.register(Concepto, ConceptoAdmin)
