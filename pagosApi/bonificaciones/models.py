from common.models import models, AbstractBaseModel


class Bonificacion(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    percentage = models.FloatField()

    def __str__(self) -> str:
        return f"bonificacion {self.title}"
