from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Pasajero(models.Model):
    nombre = models.CharField(max_length=200)
    ci = models.CharField()

    def __str__(self):
        return f'{self.nombre} ({self.ci})'

class Reserva(models.Model):
    pasajero = models.ForeignKey(Pasajero, related_name='pasajero_reservas', on_delete=models.CASCADE)
    viaje = models.ForeignKey('rutas.Viaje', related_name='viaje_reservas', on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    ESTADOS = [
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
        ('TRANSFERIDA', 'Transferida'),
    ]
    
    estado = models.CharField(max_length=20, choices=ESTADOS, default='CONFIRMADA')

    precio = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"Reserva {self.id} - Pasajero {self.pasajero} - Viaje {self.viaje}"