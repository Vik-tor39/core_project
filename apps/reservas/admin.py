from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
@admin.register(Pasajero)
class PasajeroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ci',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('bus__cooperativa__nombre', 'pasajero', 'asiento')
    # form = ReservaForm