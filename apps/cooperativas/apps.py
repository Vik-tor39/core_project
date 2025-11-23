from django.apps import AppConfig


class CooperativasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.cooperativas'

    # registro de señal:
    def ready(self):
        import apps.cooperativas.signals