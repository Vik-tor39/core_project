from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Cooperativa)
def crear_config_coop(sender, instance, created, **kwargs):

    if kwargs.get('raw', False):
        return

    if created:
        try:
            # Si ya existe, no hacer nada
            instance.configuracion 
        except Cooperativa.configuracion.RelatedObjectDoesNotExist:
            # Si no existe, se crea aquí
            ConfiguracionCoop.objects.create(orden=instance)
    
    # if created:
    #     ConfiguracionCoop.objects.create(cooperativa = instance)