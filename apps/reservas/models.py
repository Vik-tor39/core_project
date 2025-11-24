from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Pasajero(models.Model):
    nombre = models.CharField(max_length=200)
    ci = models.CharField()

    def __str__(self):
        return f'{self.nombre} ({self.ci})'

class Reserva(models.Model):
    asiento = models.PositiveIntegerField()
    pasajero = models.ForeignKey(Pasajero, related_name='pasajero_reservas', on_delete=models.CASCADE)
    bus = models.ForeignKey('rutas.Bus', related_name='bus_reservas', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (('asiento', 'bus'),)

    def clean(self):
        super().clean()
        if self.asiento and self.bus:
            if self.asiento > self.bus.capacidad:
                raise ValidationError('Este número de asiento no existe en el bus.')