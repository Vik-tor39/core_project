from django.contrib import admin
from .models import *
from .forms import *

# Inlines:
class ConfiguracionCoopInline(admin.StackedInline):
    model = ConfiguracionCoop
    can_delete = False
    verbose_name = "Configuración"

# Register your models here.
@admin.register(Cooperativa)
class CooperativaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    inlines = [ConfiguracionCoopInline]
    # form = CooperativaForm

@admin.register(ConfiguracionCoop)
class ConfiguracionCoopAdmin(admin.ModelAdmin):
    search_fields = ('cooperativa__nombre',)