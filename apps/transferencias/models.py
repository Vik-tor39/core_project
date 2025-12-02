from django.db import models

# Create your models here.
class Transferencia(models.Model):
    sugerencia = models.OneToOneField('sugerencias.SugerenciaTransferencia', related_name='transferencia', on_delete=models.CASCADE)
    pasajeros_transferidos = models.PositiveBigIntegerField()
    comision_generada = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transferencia {self.id} - Sug {self.sugerencia.id}"