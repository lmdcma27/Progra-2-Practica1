from django.shortcuts import render, redirect  
from django.http import HttpResponse, HttpResponseRedirect
from apps.registro.forms import formulario
from apps.registro.models import Usuario
from django.core.mail import send_mail
from django.conf import settings
import re
# Create your views here.
    

def registro(request):
    if request.method == 'POST':
        form = formulario(request.POST)
        verificarcorreo = re.match(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.]+', request.POST['correo'])            
        booleano = bool(verificarcorreo)
        if form.is_valid():
            if booleano == True:    
                form.save()
                correo = request.POST['correo']
                nombre = request.POST['nombre']
                contra = request.POST['contra']
                asunto = 'Su cuenta ha sido registrada, para validarla ingrese al siguiente link: http://127.0.0.1:8000/registro/direccion/unica/creada/para/validar/cuenta/atraves/de/correo/electronico/'
                email_from = settings.EMAIL_HOST_USER
                email_to = [correo]
                mensaje = "tu contraseña es: %s" %(contra)
                send_mail(asunto, mensaje, email_from, email_to, fail_silently = False)
                return HttpResponse("Acceda a su correo para validar la cuanta")
            else:
                return HttpResponse("No ha ingresado una expresión de correo válida, volver a intentar")
    else:
        form = formulario()
    
    return render(request,'registro/formular.html', {'form': form})

def validacion(request):
    x = "Tu cuenta ha sido validada con exito."
    return render(request, 'registro/validacion.html',{'x': x} )
    