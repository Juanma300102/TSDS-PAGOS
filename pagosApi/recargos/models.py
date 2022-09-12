from common.models import models, AbstractBaseModel

class Recargo(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    percentage = models.FloatField()

    def __str__(self) -> str:
        return f"Recargo {self.title}"
