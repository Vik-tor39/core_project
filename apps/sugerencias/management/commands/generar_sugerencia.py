from django.core.management.base import BaseCommand
from apps.sugerencias.services import generar_sugerencias

class Command(BaseCommand):
    help = 'Genera sugerencias de transferencia'
    
    def handle(self, *args, **options):
        creadas = generar_sugerencias()
        self.stdout.write(f"Sugerencias creadas: {len(creadas)}")