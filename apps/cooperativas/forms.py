from django import forms
from .models import *

province_codes_dict = {
    "01": "Azuay", "02": "Bolívar", "03": "Cañar", "04": "Carchi", "05": "Cotopaxi",
    "06": "Chimborazo", "07": "El Oro", "08": "Esmeraldas", "09": "Guayas", "10": "Imbabura",
    "11": "Loja", "12": "Los Ríos", "13": "Manabí", "14": "Morona Santiago", "15": "Napo",
    "16": "Pastaza", "17": "Pichincha", "18": "Tungurahua", "19": "Zamora Chinchipe",
    "20": "Galápagos", "21": "Sucumbíos", "22": "Orellana", "23": "Santo Domingo de los Tsachilas",
    "24": "Santa Elena"
}

only_codes = list(province_codes_dict.keys())

class CooperativaForm(forms.ModelForm):
    class Meta:
        model = Cooperativa
        fields = ['nombre', 'ruc', 'acuerdo_comision']

    def clean_ruc(self):
        ruc = self.cleaned_data['ruc']
        
        if not ruc.isdigit() or ruc[-3:] != '001' or not ruc[:2] in only_codes or ruc[2] != '9':
            raise forms.ValidationError('No se pudo guardar la cooperativa')

        return ruc