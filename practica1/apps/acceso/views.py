from django.shortcuts import render, redirect  
from django.http import HttpResponse, HttpResponseRedirect 
from apps.registro.models import Usuario
from apps.acceso.forms import loginform
from apps.registro.forms import formulario
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def obtener_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
    



@login_required
def acceso(request):
    fechatiempo = datetime.now()
    fecha = fechatiempo.strftime("%Y-%m-%d")
    hora = fechatiempo.strftime("%H:%M:%S")
    obtener_ip(request)
    form = loginform(request.POST or None)  
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            nombre = data.get("nombre")
            correo = data.get('correo')
            contra = data.get("contra")
            asunto = "Usted accedio a su cuenta el dia "+ fecha + " a las " + hora, " desde la ip: " + obtener_ip(request)
            email_from = settings.EMAIL_HOST_USER
            email_to = [correo]
            mensaje = "tu contraseña es: %s" %(contra)
            send_mail(asunto, mensaje, email_from, email_to, fail_silently = False)
            if Usuario.objects.filter(pk=nombre).count():
                aux = Usuario.objects.get(pk=nombre)
                if aux.nombre == nombre and aux.correo == correo and aux.contra == contra:
                    acc = authenticate(username=nombre, password= contra)            
                    login(request, acc)                                        
                    return HttpResponseRedirect(reverse('perfil', kwargs= {'nombre':nombre}))                    
                else: 
                    return HttpResponse("Correo y/o contraseña invalidos, volvé a intentar")
            else:
                return HttpResponse(" El usuario no existe.")
                
    else:
        form = loginform()

    contexto = {'form': form}
    return render(request, 'acceso/acceso.html', contexto)


def perfil(request, nombre):
    usuario = Usuario.objects.get(pk=nombre)
        
    if request.method == "GET":
        form = formulario(instance=usuario)

    else:
        form = formulario(request.POST, instance=usuario) 
        if form.is_valid():
            form.save()   
            return redirect('acceso')            
      
    return render(request, 'acceso/perfil.html', {'form': form}) 
