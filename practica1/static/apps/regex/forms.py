from django import forms 
from .models import Regex

class regexform(forms.ModelForm):
    class Meta:
        model = Regex

        fields = ('regex',)

        labels = {
            'regex': 'Ingrese su Expresion Regular',
        }

        widgets = {
            'regex': forms.TextInput(attrs={'class':'form-control'}),
        }



