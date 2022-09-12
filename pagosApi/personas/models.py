from multiprocessing.util import abstract_sockets_supported
from pyexpat import model
from common.models import models, AbstractBaseModel

class Persona(AbstractBaseModel):
    firtname = models.TextField()
    lastname = models.TextField()
    dni = models.FloatField()
    birthdate = models.DateField()

    def __str__(self) -> str:
        return f"Persona {self.firtname} {self.lastname}"
        
