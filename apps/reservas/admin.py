from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
@admin.register(Pasajero)
class PasajeroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ci',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'viaje__id', 'pasajero', 'precio')
    # form = ReservaForm