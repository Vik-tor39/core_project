from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('origen', 'destino',)

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('cooperativa__nombre', 'ruta', 'ocupacion_actual', 'capacidad', 
                    'porcentaje_ocupacion', 'cooperativa__configuracion__umbral_ocupacion')
    # form = BusForm
    # readonly_fields = ('ocupacion_actual',)