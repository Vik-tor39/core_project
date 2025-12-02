from django.db import transaction
from decimal import Decimal
from apps.sugerencias.models import SugerenciaTransferencia
from .models import Transferencia
from django.db.models import F

def procesar_transferencia(sugerencia_id, operador="system"):
    
    with transaction.atomic():
    
        sugerencia = SugerenciaTransferencia.objects.select_for_update().select_related(
            'bus_origen__cooperativa', 'bus_destino__cooperativa').get(id=sugerencia_id)

        if sugerencia.estado != 'PENDIENTE':
            raise ValueError('Sugerencia no está en estado pendiente')
        
        origen = sugerencia.bus_origen
        destino = sugerencia.bus_destino
        cantidad_psj = sugerencia.pasajeros_sugeridos

        # Revalidación de recursos antes de mover pasajeros
        if origen.ocupacion_actual < cantidad_psj:
            raise ValueError("El bus origen ya no tiene suficientes pasajeros.")

        espacio_disp = destino.capacidad - destino.ocupacion_actual
        if espacio_disp < cantidad_psj:
            raise ValueError("El bus destino ya no tiene espacio suficiente.") 
        
        
        # Actualizar ocupaciones:
        origen.ocupacion_actual = F('ocupacion_actual') - cantidad_psj
        destino.ocupacion_actual = F('ocupacion_actual') + cantidad_psj

        origen.save(update_fields=['ocupacion_actual'])
        destino.save(update_fields=['ocupacion_actual'])


        # Cálculo de comisión:
        porcentaje = origen.cooperativa.acuerdo_comision or Decimal('0.0')
        # Por el momento: comisión = pasajeros * porcentaje
        comision = Decimal(cantidad_psj) * Decimal(porcentaje)

        
        # Registrar en tabla Transferencia
        transferencia = Transferencia.objects.create(
            sugerencia=sugerencia,
            pasajeros_transferidos=cantidad_psj,
            comision_generada = comision
        )

        # marcar sugerencia aceptada
        sugerencia.estado = 'ACEPTADA'
        sugerencia.save()

        # Por el momento no hay procesamiento de transferencia en tabla de reservas

        return transferencia