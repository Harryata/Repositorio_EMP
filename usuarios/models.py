from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=15, verbose_name="Número de Teléfono")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")

    def __str__(self):
        return f"{self.username} - {self.email}"
