from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse
from .forms import tablaform
from .models import Tabla
from apps.regex.views import Algoritmo



def tabla(request):
    
    form = tablaform(request)
    if request.method == 'POST':
        if request.POST['tabla'] != "":
            return HttpResponseRedirect(reverse('expresion', kwargs={'re': request.POST['tabla']}))
    else:
        form = tablaform()

    return render(request, 'tabla/tabla.html', {'form': form})

def expresion(request, re):

    lista = []
    instancia = Algoritmo()
    er = instancia.convertir(re)
    for claves, valores in er[0].items():
        lista.append([claves[0], claves[1], valores])
    
    return render(request, 'tabla/expresion.html', {'lista': lista, 'er': er[1]})


