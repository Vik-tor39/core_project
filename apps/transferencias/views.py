from django.shortcuts import render, redirect, get_object_or_404
from .services import procesar_transferencia
from apps.sugerencias.models import SugerenciaTransferencia

# Create your views here.
def panel_sugerencias(request):
    sugerencias = SugerenciaTransferencia.objects.filter(estado='PENDIENTE').select_related('bus_origen','bus_destino')
    return render(request, 'transferencias/panel_sugerencias.html', {'sugerencias': sugerencias})

def aceptar_sugerencia(request, sug_id):
    if request.method == 'POST':
        sugerencia = get_object_or_404(SugerenciaTransferencia, id=sug_id)
        procesar_transferencia(sugerencia.id, operador=request.user.username if request.user.is_authenticated else 'anon')
    return redirect('panel_sugerencias')