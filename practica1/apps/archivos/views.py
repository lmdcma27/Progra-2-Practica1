from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse
from .forms import archivosform, editarform
from .models import Archivos
from apps.registro.models import Usuario
from django.core.files import File
import re 
# Create your views here.

def automata(archivo):    
    digitos = ['0','1','2','3','4','5','6','7','8','9']
    pinteres = ['teorema', 'Matemático', 'Matemática', 'Hilbert', 'Turing', 'análisis',
        'Euler', 'Fermat', 'Pitágoras', 'automata', 'Boole', 'Cantor', 'Perelman'
        'Experimentación', 'Físico', 'Física', 'Astronomía', 'Mecánica', 'Newton',
        'Einstein', 'Galileo', 'Modelo', 'Dinámica', 'Partículas'] 
    
    estado_actual = 0
    estados_aceptacion = [1,4,6,7,8,9,18,22,27,30,31,32,34,35]
    #definimos la función de transición
    transicion = {
       (0,'d'): 1, (0,'+'): 2, (0,'-'): 3, (0,'i'): 4, (1,'.'): 5, (1,'d'): 6,
       (1,'+'): 36, (1,'-'): 36, (6,'+'): 36, (6,'-'): 36, (7,'+'): 36, 
       (7,'-'): 36, (36,'d'): 36, (36,'i'): 4, (2,'d'): 7, (3,'d'): 7,
       (4,'d'): 8, (5,'d'): 9, (6,'.'): 5, (6,'d'): 7, (6,'/'): 10, (6,'-'): 11,
       (7,'d'): 7, (7,'.'): 5, (8,'d'): 8, (8,'.'): 12, (9,'d'): 9, (9,'+'): 13,
       (9,'-'): 14, (9,'x'): 15, (10,'d'): 16, (11,'d'): 17, (12,'d'): 35,
       (35,'d'): 35, (13,'i'): 18, (14,'i'): 18, (15,'e'): 19, (16,'d'): 20,
       (17,'d'): 21, (18,'d'): 22, (19,'+'): 23, (19,'-'): 23, (20,'/'): 24,
       (21,'-'): 25, (22,'d'): 22, (22,'.'): 26, (23,'d'): 27, (24,'d'): 28,
       (25,'d'): 29, (26,'d'): 30, (27,'d'): 27, (28,'d'): 31, (29,'d'): 32,
       (30,'d'): 30, (31,'d'): 33, (33,'d'): 34,
    }

    texto = open(archivo, 'r')
    lista = []
    for readline in texto:

        for cadena in readline.split(" "):
                
            compilar = re.compile(r'\d\d\/\d\d\/\d\d\d\d|\d\d\/\d\d\/\d\d|\d\d-\d\d-\d\d|(\+|-)?\d+\.\d+xe(\+|-)?\d+|(\+|-)?(\d+\.\d+|\d+)(\+|-)i(\d+\.\d+|\d*)|(\+|-)?i(\d+\.\d+|\d+)|(\+|-)?\d+\.\d+|(\+|-)?\d+')
            filtro = compilar.finditer(cadena)
            for x in filtro:
                string = cadena[x.span()[0]:x.span()[1]]
                estado_actual = 0
                for caracter in string:
                    if (estado_actual, caracter) in transicion:
                        estado_actual = transicion[(estado_actual, caracter)]
                    elif caracter in digitos:
                        caracter = 'd'
                        estado_actual = transicion[(estado_actual, caracter)]
                    else:
                        estado_actual ="no aceptado"
                        break
            
                if estado_actual in estados_aceptacion:
                    if estado_actual == 1 or estado_actual == 6 or estado_actual == 7:
                        lista.append([string, "blue"])
                        print(estado_actual)
                        print("cadena aceptada")
                    if estado_actual == 9:
                        lista.append([string, "green"])
                    if estado_actual == 4 or estado_actual == 8 or estado_actual == 18 or estado_actual == 22 or estado_actual == 30 or estado_actual == 35:
                        lista.append([string, "red"])
                    if estado_actual == 27:
                        lista.append([string, "purple"])
                    if estado_actual == 31 or estado_actual == 33 or estado_actual == 34:
                        lista.append(string, "orange")
     
                else:
                    estado_actual = "cadena no aceptada"
                    
    temp = texto.read()
    listapalabra = []
    for palabra in pinteres:
        if palabra in temp:
            listapalabra.append([palabra, "grey"])
    texto.close()
    return lista, listapalabra


def archivos_subidos(request, nombre):
    n = Usuario.objects.get(pk=nombre).nombre
    arch = Archivos.objects.all() 
    for i in arch:
        if i.propietario.nombre == nombre:                                                                          
            h = open(i.archivo.path, 'r')
            i.texto = h.read()
            i.save()                            
            h.close()

    return render(request, 'archivos/archivos_subidos.html',
     {'arch':arch, 'n': n})

def editar(request, documento):
    f = Archivos.objects.all()
    form = editarform(request.POST)                
    for x in f:
        if x.archivo.name == documento:
            aux = x
    if request.method == 'GET':       
        form = editarform(instance=aux)
    else:
        form = editarform(request.POST, instance=aux)
        if form.is_valid():
            form.save()
            h = open(aux.archivo.path, 'w')            
            h.write(aux.texto)
            h.close()
    return render(request, 'archivos/editar_archivos.html', {'form': form,'f': f, 'd': documento,})

def archivar(request):
    if request.method == 'POST':
        form = archivosform(request.POST, request.FILES)
        name = request.POST['propietario']
        password = request.POST['password']
        clave = request.FILES['archivo'].name[-3:] 
        f = Archivos.objects.all()            
        booleano = False
        for x in f:
            if x.propietario.nombre == name:
                if x.archivo.name == request.FILES['archivo'].name:
                    booleano = True
                
        temp = Usuario.objects.filter(pk= name)
        if form.is_valid() and booleano == False:
            if temp.count() and password == Usuario.objects.get(pk=name).contra:                
                if clave == ".p2":
                    form.save()                    
                    return HttpResponseRedirect(reverse('archivos_subidos', kwargs= {'nombre':name}))                    
                else:
                    return redirect('error_extension')    
            else:
                return redirect('error_usuario')
        else: 
            return HttpResponse("Este archivo ya fue subido")
    else:    
        form = archivosform()

    return render(request, 'archivos/archivar.html', {'form': form})



def error_usuario(request):
    return render(request, 'archivos/error_usuario.html')

def error_extension(request):
    return render(request, 'archivos/error_extension.html')