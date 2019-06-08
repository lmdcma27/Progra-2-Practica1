from django import forms 
from .models import Archivos

class archivosform(forms.ModelForm):
    class Meta:
        model = Archivos

        fields = ('propietario', 'password', 'archivo')

        labels = {
            'propietario': 'Nombre',
            'password': 'Contraseña',
            'archivo': 'Archivo',
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'form-control'}),  
        }

class editarform(forms.ModelForm):
    class Meta:
        model = Archivos
        
        fields = [            
            'texto',
        ]
        
        labels = {                                    
            'texto': '',        
        }

        widgets = {            
            'texto': forms.Textarea(attrs={'class':'form-control', 'cols': 100, 'rows': 14}),
           
        }
