from django import forms
from .models import *

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

    def clean(self):
        clean_data = super().clean()
        asiento = clean_data.get('asiento')
        bus = clean_data.get('bus')

        if asiento and bus.capacidad:
            if asiento > bus.capacidad:
                raise forms.ValidationError('No se puede asignar el nuevo asiento.')