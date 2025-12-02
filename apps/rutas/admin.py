from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('origen', 'destino',)

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('cooperativa__nombre', 'capacidad',)
    # form = BusForm
    # readonly_fields = ('ocupacion_actual',)

@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    list_display = ('bus', 'ruta', 'fecha', 'hora_salida')