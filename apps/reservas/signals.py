from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
@receiver(post_save, sender=Reserva)
def aumentar_capacidad_actual(sender, instance, created, **kwargs):
    if created:
        bus = instance.bus
        bus.ocupacion_actual = bus.bus_reservas.count()
        bus.save(update_fields=['ocupacion_actual'])