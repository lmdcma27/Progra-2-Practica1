from django import forms 
from .models import Tabla


class tablaform(forms.ModelForm):
    class Meta:
        model = Tabla
        
        
        fields = ('tabla',)

        labels = {
            'tabla': 'Escoger Expresión',
            
        }

        widgets = {
            'tabla': forms.Select(attrs={'class':'form-control'}),
           
        }