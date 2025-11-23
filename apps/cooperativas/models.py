from django.db import models

# Create your models here.
class Cooperativa(models.Model):
    nombre = models.CharField(max_length=150)
    ruc = models.CharField(unique=True, max_length=13)
    acuerdo_comision = models.DecimalField(max_digits=5, decimal_places=2, default=0.10)

    def __str__(self):
        return self.nombre

class ConfiguracionCoop(models.Model):
    umbral_ocupacion = models.PositiveIntegerField(default=0)
    ventana_tiempo = models.PositiveIntegerField(default=0)
    cooperativa = models.OneToOneField(Cooperativa, related_name='configuracion', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Configuración: {self.cooperativa}'