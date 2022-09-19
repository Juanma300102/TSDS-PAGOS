from conceptos.models import Concepto
from common.models import AbstractBaseModel, models
from suscripciones.models import Suscripcion
from periodos.models import Periodo


class Deuda(AbstractBaseModel):
    suscripcion = models.ForeignKey(Suscripcion, models.RESTRICT)
    period = models.ForeignKey(Periodo, models.RESTRICT)

    def __str__(self) -> str:
        return f"Deuda de {self.suscripcion.persona.firstname} {self.suscripcion.persona.lastname} por el servicio {self.suscripcion.service.title}"
