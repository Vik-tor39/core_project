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
    ocupacion_actual = models.PositiveIntegerField(default=0)
    hora_salida = models.DateTimeField()
    cooperativa = models.ForeignKey('cooperativas.Cooperativa', related_name='coop_buses', on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, related_name='ruta_buses', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'bus'
        verbose_name_plural = 'buses'

    # Validación personalizada:
    def clean(self):
        super().clean()
        if self.ocupacion_actual and self.capacidad and self.ocupacion_actual > self.capacidad:
            raise ValueError('La ocupación actual no puede superar a la capacidad total')

    def __str__(self):
        return f'{self.cooperativa} Bus'