from common.models import models, AbstractBaseModel


class MontoBase(AbstractBaseModel):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self) -> str:
        return f"{self.amount} valid until {self.valid_until}"
