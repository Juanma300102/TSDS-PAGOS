from common.models import models, AbstractBaseModel
from personas.models import Persona
from servicios.models import Servicio


class Suscripcion(AbstractBaseModel):
    person = models.ForeignKey(Persona, models.RESTRICT)
    service = models.ForeignKey(Servicio, models.RESTRICT)

    def __str__(self) -> str:
        return f"Suscripcion de {self.person.firstname} {self.person.lastname} a {self.service.title}"
