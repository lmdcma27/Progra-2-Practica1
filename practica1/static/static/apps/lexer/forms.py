from django import forms 
from .models import Lexer


class selecform(forms.ModelForm):
    class Meta:
        model = Lexer
        
        
        fields = ('cadena', 'texto')

        labels = {
            'cadena': 'Escoger Expresión',
            'texto': 'Ingresar Texto',
        }

        widgets = {
            'cadena': forms.Select(attrs={'class':'form-control'}),
            'texto': forms.Textarea(attrs={'class':'form-control'}),
        }