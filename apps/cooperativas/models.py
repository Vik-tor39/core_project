from django.db import models
from django.core.exceptions import ValidationError

# Validación personalizada de 'ruc':
def validate_ruc(value):

    # province codes:
    prv_codes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', 
                '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

    if (
        len(value) != 13 or
        not value.isdigit() or
        value[:2] not in prv_codes or
        value[2] != '9' or
        not value.endswith('001')
    ):
        raise ValidationError('El valor del RUC no es válido.')
    

# Create your models here.
class Cooperativa(models.Model):
    nombre = models.CharField(max_length=150)
    ruc = models.CharField(unique=True, max_length=13, validators=[validate_ruc])
    acuerdo_comision = models.DecimalField(max_digits=5, decimal_places=2, default=0.10)

    def __str__(self):
        return self.nombre

class ConfiguracionCoop(models.Model):
    umbral_ocupacion = models.PositiveIntegerField(default=0)
    ventana_tiempo = models.PositiveIntegerField(default=0)
    cooperativa = models.OneToOneField(Cooperativa, related_name='configuracion', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Configuración: {self.cooperativa}'