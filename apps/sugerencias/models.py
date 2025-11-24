from django.db import models

# Create your models here.
class SugerenciaTransferencia(models.Model):
    ESTADO_CHOICES = {
        'PENDIENTE': 'pendiente',
        'ACEPTADA': 'aceptada',
        'RECHAZADA': 'Rechazada',
    }
    bus_origen = models.ForeignKey('rutas.Bus', related_name='sugerencia_origen', on_delete=models.CASCADE)
    bus_destino = models.ForeignKey('rutas.Bus', related_name='sugerencia_destino', on_delete=models.CASCADE)
    pasajeros_sugeridos = models.PositiveIntegerField()
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='PENDIENTE')

    def __str__(self):
        return f'{self.bus_origen} --> {self.bus_destino} (mover {self.pasajeros_sugeridos} pasajeros)'