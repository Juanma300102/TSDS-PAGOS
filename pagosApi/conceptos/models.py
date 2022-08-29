from common.models import models, AbstractBaseModel
from montosBase.models import MontoBase


class Concepto(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.ForeignKey(MontoBase, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f"Concepto {self.pk} : {self.title} | amount : {self.amount}"
