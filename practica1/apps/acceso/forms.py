from django import forms 
from apps.registro.models import Usuario 

class loginform(forms.Form):
        nombre = forms.CharField(max_length=50, required= True, label="",
            widget=(forms.TextInput(attrs={"placeholder":"Nombre de Usuario",
            "class":"input-login"})))

        correo = forms.CharField(max_length=50, required= True, label="",
            widget=(forms.TextInput(attrs={"placeholder":"Correo",
            "class":"input-login"})))
        
        contra = forms.CharField(max_length=50, required= True, label="",
            widget=(forms.PasswordInput(attrs={"placeholder":"Contraseña",
            "class":"input-login"})))


    
