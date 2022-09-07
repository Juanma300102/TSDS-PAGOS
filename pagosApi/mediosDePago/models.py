from common.models import models, AbstractBaseModel


class MedioDePago(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return f"Medio de pago : {self.title}"
