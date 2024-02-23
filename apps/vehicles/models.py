from django.db import models
from apps.users.models import User


def default_last_position():
    return {"lat": "", "lng": ""}


class Vehicle(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Usuario', on_delete=models.CASCADE
    )
    plates = models.CharField(
        verbose_name='Placas', max_length=255
    )
    last_position = models.JSONField(
        verbose_name='Ultima posicion', default=default_last_position
    )

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'

    def __str__(self):
        return f'{self.plates}'