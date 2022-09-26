from common.models import AbstractBaseModel, models
from personas.models import Persona
from mediosDePago.models import MedioDePago
from deudas.models import Deuda


class PagoADeuda(AbstractBaseModel):
    persona = models.ForeignKey(Persona, models.RESTRICT)
    deuda = models.ForeignKey(Deuda, models.RESTRICT)
    medios_de_pagos = models.ForeignKey(MedioDePago, models.RESTRICT)
    monto = models.FloatField()


# Create your models here.
