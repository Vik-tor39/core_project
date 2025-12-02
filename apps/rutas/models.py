from django.db import models

# Create your models here.
class Ruta(models.Model):
    origen = models.CharField(max_length=150)
    destino = models.CharField(max_length=150)

    class Meta:
        unique_together = (('origen', 'destino'),)

    def __str__(self):
        return f'{self.origen} --> {self.destino}'
        
class Bus(models.Model):
    capacidad  = models.PositiveIntegerField()
    cooperativa = models.ForeignKey('cooperativas.Cooperativa', related_name='coop_buses', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'bus'
        verbose_name_plural = 'buses'

    def __str__(self): 
        return f'{self.id} - {self.cooperativa} - {self.capacidad}'
    
class Viaje(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name='ruta_viajes')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='bus_viajes')
    fecha = models.DateField()
    hora_salida = models.TimeField()

    # estado del viaje
    ESTADOS = [
        ('PROGRAMADO', 'Programado'),
        ('EN_RUTA', 'En ruta'),
        ('FINALIZADO', 'Finalizado'),
        ('CANCELADO', 'Cancelado'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PROGRAMADO')

    class Meta:
        unique_together = ('bus', 'fecha', 'hora_salida')  # Prevenir duplicados
        ordering = ['fecha', 'hora_salida']

    def __str__(self):
        return f"Viaje {self.ruta.origen}-{self.ruta.destino} | {self.fecha} {self.hora_salida} | Bus {self.bus.codigo}"
    
    @property
    def ocupacion_actual(self):
        # Obtener # de reservas activas
        return self.viaje_reservas.filter(estado='CONFIRMADA').count()

    @property
    def capacidad(self):
        # Obtener capacidad del viaje proveniente de bus
        return self.bus.capacidad

    @property
    def porcentaje_ocupacion(self):
        if self.capacidad == 0:
            return 0
        return (self.ocupacion_actual / self.capacidad) * 100