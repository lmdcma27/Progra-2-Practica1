from django import forms 
from apps.registro.models import Usuario 

class formulario(forms.ModelForm):
        
    class Meta:
        model = Usuario
        fields = [ 
            'nombre',
            'carnet',
            'correo',
            'cui',
            'profesion',
            'contra',

        ]
        labels = {
            'nombre': 'Nombre',
            'carnet': 'Carnet',
            'correo': 'Correo',
            'cui': 'Cui',
            'profesion': 'Profesión',
            'contra': 'Contraseña',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'carnet': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'cui': forms.TextInput(attrs={'class':'form-control'}),
            'profesion': forms.Select(attrs={'class':'form-control'}),
            'contra': forms.PasswordInput(attrs={'class':'form-control'}),
        }
