from django import forms
from .models import *

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'  # Enviar todos los campos al formulario dado que se este form se usara en el panel admin

    def clean(self):
        cleaned_data = super().clean()
        capacidad = cleaned_data.get('capacidad')
        ocupacion_actual = cleaned_data.get('ocupacion_actual')

        if ocupacion_actual and capacidad:

            if ocupacion_actual > capacidad:
                raise forms.ValidationError('La ocuapación actual no puede ser superior a la capacidad total.')