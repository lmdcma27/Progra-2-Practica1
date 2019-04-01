from django import forms 
from .models import Archivos

class archivosform(forms.ModelForm):
    class Meta:
        model = Archivos

        fields = ('name', 'password', 'archivo')

        labels = {
            'name': 'Nombre',
            'password': 'Contraseña',
            'archivo': 'Archivo',
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'control-form'}),
        }