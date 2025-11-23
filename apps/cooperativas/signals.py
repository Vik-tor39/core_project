from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Cooperativa)
def crear_config_coop(sender, instance, created, **kwargs):
    if created:
        ConfiguracionCoop.objects.create(cooperativa = instance)