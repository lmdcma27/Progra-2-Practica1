from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse
from .forms import archivosform
from .models import Archivos
from apps.registro.models import Usuario
# Create your views here.

def archivos_subidos(request, nombre):
    n = Usuario.objects.get(pk=nombre).nombre
    arch = Archivos.objects.all()           
                      
    return render(request, 'archivos/archivos_subidos.html',
     {'arch':arch, 'n': n})


def archivar(request):
    if request.method == 'POST':
        form = archivosform(request.POST, request.FILES)
        name = request.POST['name']
        password = request.POST['password']
        clave = request.FILES['archivo'].name[-3:]        
        temp = Usuario.objects.filter(pk= name)
        if form.is_valid():
            if temp.count() and password == Usuario.objects.get(pk=name).contra:                
                if clave == ".p2":
                    form.save()
                    return HttpResponseRedirect(reverse('archivos_subidos', kwargs= {'nombre':name}))                    
                else:
                    return redirect('error_extension')    
            else:
                return redirect('error_usuario')

    else:    
        form = archivosform()

    return render(request, 'archivos/archivar.html', {'form': form})



def error_usuario(request):
    return render(request, 'archivos/error_usuario.html')

def error_extension(request):
    return render(request, 'archivos/error_extension.html')