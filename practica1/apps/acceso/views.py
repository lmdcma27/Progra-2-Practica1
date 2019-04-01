from django.shortcuts import render, redirect  
from django.http import HttpResponse, HttpResponseRedirect 
from apps.registro.models import Usuario
from apps.acceso.forms import loginform
from apps.registro.forms import formulario
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def acceso(request):

    form = loginform(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            nombre = data.get("nombre")
            correo = data.get('correo')
            contra = data.get("contra")
            
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
