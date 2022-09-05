from conceptos.models import Concepto
from common.models import AbstractBaseModel, models


class Servicio(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    concept = models.ForeignKey(to=Concepto, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f"Servicio: {self.title}"
