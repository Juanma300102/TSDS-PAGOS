from pyexpat import model
from common.models import AbstractBaseModel, models


class Periodo(AbstractBaseModel):
    title = models.CharField(max_length=100)
    late = models.DateField()

    def __str__(self) -> str:
        return f"Periodo {self.title}"
