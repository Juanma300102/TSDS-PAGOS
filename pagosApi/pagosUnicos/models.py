from common.models import AbstractBaseModel, models
from personas.models import Persona
from mediosDePago.models import MedioDePago
from conceptos.models import Concepto


class PagoUnico(AbstractBaseModel):
    persona = models.ForeignKey(Persona, models.RESTRICT)
    concepto = models.ForeignKey(Concepto, models.RESTRICT)
    medios_de_pagos = models.ForeignKey(MedioDePago, models.RESTRICT)


# Create your models here.
