from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse
from .forms import selecform
from .models import Lexer
from apps.regex.views import Algoritmo


# Create your views here.

def automata(texto, diccionario, conjunto_aceptacion, qinicial):
        lista1 = []        
        lista2 = []
        for palabra in texto.split(): 
                estado_actual = qinicial                
                for letra in palabra:
                        if (estado_actual, letra) in diccionario:                                
                                estado_actual = diccionario[(estado_actual,letra)]                                                        
                        else:
                                estado_actual = "cadena rechazada"

                if estado_actual in conjunto_aceptacion:
                        lista1.append(palabra)                        
                        lista2.append("blue")
                        
                else:
                        lista1.append(palabra)                        
                        lista2.append("black")
                        
                
        return lista1, lista2

def lexer(request):

        
    prueba = selecform(request.POST)

    if request.method == 'POST':     
        if prueba.is_valid():
            if request.POST['cadena'] != "":
                objeto = request.POST['cadena']
                objetos = Lexer.objects.all()
                exsite = True
                for elemento in objetos:
                    if objeto == elemento.cadena.regex:
                        elemento.delete()                                             
                prueba.save()      
            else:
                    return HttpResponse("Debe seleccionar una expresión regular")

        if prueba.is_valid():
                return HttpResponseRedirect(reverse('resultado', kwargs= {'cadena': request.POST['cadena']}))                    

        
    return render(request, 'lexer/lexer.html', {'prueba': prueba})


def resultado(request, cadena):
        objetos = Lexer.objects.all()
        for objeto in objetos:                
            if objeto.cadena.regex == cadena:
                texto = objeto.texto
                expresion = cadena
                break

        instancia = Algoritmo()
        r = instancia.convertir(expresion)
        lista = automata(texto, r[0], r[1], r[2])

        return render( request, 'lexer/resultado.html', {'lista1': lista[0], 'lista2': lista[1], 'cadena': cadena})
