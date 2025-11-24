from apps.rutas.models import *
from apps.cooperativas.models import *
from .models import SugerenciaTransferencia
from django.db.models import F

# Motor básico: por cada bus con ocupacion < umbral, buscar un destino con espacio
def generar_sugerencias(limiti_por_origen=5):
    buses = Bus.objects.select_related('cooperativa', 'ruta')
    sug_creadas = []

    for bus in buses:
        config = getattr(bus.cooperativa, 'configuracion', None)
        if not config:
            continue
        
        if bus.porcentaje_ocupacion < config.umbral_ocupacion:
            # buscar destino bajo misma ruta con espacio disponible:
            destinos = Bus.objects.filter(ruta=bus.ruta).exclude(id=bus.id).annotate(espacio=F('capacidad')-F('ocupacion_actual')).filter(espacio__gt=0).order_by('-espacio')

            if destinos.exists():
                destino = destinos.first()
            
            # decidir mínimo de pasajeros entre total de espacio de destino o limite (así se evita grandes transferencias):
            sugerido = min(destino.capacidad - destino.ocupacion_actual, limiti_por_origen)
            if sugerido <= 0:
                continue

            s = SugerenciaTransferencia.objects.create(bus_origen=bus, bus_destino=destino, pasajeros_sugeridos=sugerido)
            sug_creadas.append(s)
    
    return sug_creadas