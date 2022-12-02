from django.db import models
from django.contrib.auth.models import AbstractUser


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)
    soft_deleted = models.BooleanField()

    class Meta:
        abstract = True


class User(AbstractUser):
    uuid = models.UUIDField(null=True)
