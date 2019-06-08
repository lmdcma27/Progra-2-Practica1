from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse
from .forms import regexform
from .models import Regex
from graphviz import Digraph, Graph
import sys
sys.setrecursionlimit(10000)

transiciones = {}
contador = [0]
alfanumerico = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
alcanzar = []
trans = {}
class Algoritmo:
	
	def __init__(self):
		
		self.transiciones = {}
		self.contador = [0]
		self.alfanumerico =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", 					     "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", 					     "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
		self.alcanzar = []
		self.estados_generales = []
		self.trans = {}
	def determinar(self, ei, el, ef):

		if (ei, el) in self.transiciones.keys():
			if ef in self.transiciones[(ei, el)]:
				pass
			else:
				lista = self.transiciones[(ei, el)]				
				lista.append(ef)
				self.transiciones[(ei, el)] = lista
		else:
			self.transiciones[(ei, el)] = [ef]
	
	#se crean las funciones que generan las transiciones de "*","+", "|" y "concatencacion"
	def concatenacion1(self, A):

		estado = "q" + str(self.contador[0])
		self.contador[0] += 1
		self.transiciones[(estado, A)] = ["q" + str(self.contador[0])]
		self.contador[0] += 1
	
		estados = [estado, "q" + str(self.contador[0] - 1)]
		return estados

	def concatenacion2(self, A, qinicial):
			
		estado = "q" + str(self.contador[0])
		self.determinar(qinicial, A, estado)
		self.contador[0] += 1
		
		estados = [qinicial, estado]
		return estados
	def concatenacion3(self, qfinal, qinicial):
		self.determinar( qfinal, "vacio", qinicial)

	def clausura1(self, A):
		
		estado = "q" + str(self.contador[0])
		self.contador[0] += 1
		self.determinar( estado, "vacio", "q" + str(self.contador[0]) )
		estado = "q" + str(self.contador[0])
		self.contador[0] += 1
		self.determinar( estado, A, "q" + str(self.contador[0]) )
		self.determinar( "q" + str(self.contador[0]), "vacio", estado )
		estado = "q" + str(self.contador[0])		
		self.contador[0] += 1
		self.determinar( estado, "vacio", "q" + str(self.contador[0]) )
		self.determinar( "q" + str(self.contador[0] - 3), "vacio", "q" + str(self.contador[0]) )
		self.contador[0] += 1

		estados = ["q" + str(self.contador[0] - 4),"q" + str(self.contador[0] - 1)]
		return estados

	def clausura2(self,  q, qinicial, qfinal):


		self.determinar( q , "vacio", qinicial )
		self.determinar( qfinal, "vacio", qinicial )		
		self.contador[0] += 1
		estado = "q" + str(self.contador[0])
		self.determinar( qfinal, "vacio", estado )
		self.determinar( q, "vacio", estado)
			
		self.contador[0] += 1

					
		estados = [q, estado]	
		return estados		


	def clausura3(self, qinicial, qfinal):

		estado = "q" + str(self.contador[0])
		self.determinar( estado, "vacio", qinicial )
		self.contador[0] += 1		
		self.determinar (qfinal, "vacio", qinicial)
		estado = "q" + str(self.contador[0])
		self.determinar( qfinal, "vacio", estado)
		self.determinar( "q" + str(self.contador[0] - 1), "vacio", estado  )
		estados = [ "q" + str(self.contador[0] - 1), estado]
		return estados

	def suma1(self, A):

		
		estado = "q" + str(self.contador[0])
		self.contador[0] += 1
		self.determinar( estado, "vacio", "q" + str(self.contador[0]) )
		estado = "q" + str(self.contador[0])
		self.contador[0] += 1
		self.determinar( estado, A, "q" + str(self.contador[0]) )
		self.determinar( "q" + str(self.contador[0]), "vacio", estado )
		estado = "q" + str(self.contador[0])		
		self.contador[0] += 1
		self.determinar( estado, "vacio", "q" + str(self.contador[0]) )
		self.contador[0] += 1

		estados = ["q" + str(self.contador[0] - 2), estado]	
		return estados

	def suma2(self,  q, qinicial, qfinal):


		self.determinar( q , "vacio", qinicial )
		self.determinar( qfinal, "vacio", qinicial )		
		self.contador[0] += 1
		estado = "q" + str(self.contador[0])
		self.determinar( qfinal, "vacio", estado )			
		self.contador[0] += 1

		estados = [q, estado]	
		return estados

	def suma3(self, qinicial, qfinal):

		estado = "q" + str(self.contador[0])
		self.determinar( estado, "vacio", qinicial )
		self.contador[0] += 1		
		self.determinar (qfinal, "vacio", qinicial)
		estado = "q" + str(self.contador[0])
		self.determinar( qfinal, "vacio", estado)		
		estados = [ "q" + str(self.contador[0] - 1), estado]
		return estados

	
	def barra1(self, A, qinicial, qfinal):
	
		estado = "q" + str(self.contador[0])
		self.contador[0] += 1
		self.determinar( estado, "vacio", "q"+ str(self.contador[0]) )
		estado = "q" + str(self.contador[0])
		self.contador[0] += 1
		self.determinar( estado, A, "q"+ str(self.contador[0] ) )
		self.determinar( estado, "vacio", qinicial )
		estado = "q" + str(self.contador[0])
		self.contador[0] += 1
		self.determinar(estado, "vacio", "q"+ str(self.contador[0] ) )
		self.determinar(qfinal, "vacio", "q"+ str(self.contador[0] ) )
		self.contador[0] += 1

		estados = ["q" + str(self.contador[0] - 4) ,"q" + str(self.contador[0] - 1) ]
		return estados

	def barra2(self, qinicial1, qfinal1, qinicial2, qfinal2):
		
		estado = "q" + str(self.contador[0])
		self.determinar( estado, "vacio", qinicial1 )
		self.determinar( estado, "vacio", qinicial2 )
		self.contador[0] += 1
		estado = "q" + str(self.contador[0])
		self.determinar( qfinal1, "vacio", estado )
		self.determinar( qfinal2, "vacio", estado )
		self.contador[0] += 1

		estados = ["q" + str(self.contador[0] - 2), estado]
		return estados


	def prueba1(self, A, qinicial, qfinal):
		
		estado = "q" + str(self.contador[0])		
		self.determinar( qinicial, "vacio", estado)
		self.contador[0] += 1
		del self.transiciones[(qinicial, A)]		
		self.determinar( estado, A, "q" + str(self.contador[0]) )		
		self.determinar( "q" + str(self.contador[0]), "vacio", estado )
		self.determinar( "q" + str(self.contador[0]), "vacio", qfinal)
		self.determinar( qinicial, "vacio", qfinal )							
		self.contador[0] += 1
		estados = [qinicial, qfinal]
		return estados
	
	def prueba2(self, A, qinicial, qfinal):
		
		estado = "q" + str(self.contador[0])		
		self.determinar( qinicial, "vacio", estado)
		self.contador[0] += 1
		del self.transiciones[(qinicial, A)]
		self.determinar( estado, A, "q" + str(self.contador[0]) )		
		self.determinar( "q" + str(self.contador[0]), "vacio", estado )
		self.determinar( "q" + str(self.contador[0]), "vacio", qfinal)									
		self.contador[0] += 1
		estados = [qinicial, qfinal]
		return estados


	# se emplea una funcion recursiva para generar la funcion de transicion de la expresion regular
	# leer cadena siempre debe retornar el primer y ultimo estados que genere
	def leercadena(self, cadena):

		contador = 0
		estados = []		
		#no hay anulador		
		while contador < len(cadena):
	
		#la expresion regular puede empezar por un elemento del conjunto alfanumerico o con parentesis			
				
			if cadena[contador] in self.alfanumerico:				
				
				if contador == 0:									
					estados = self.concatenacion1( cadena[contador] )										
					qinicial = estados[0]
					inicial = estados[0]
					qfinal = estados[1]	
					contador += 1					
				else:
					estados = self.concatenacion2( cadena[contador], qfinal )	
					qinicial = estados[0]				
					qfinal = estados[1]					
					contador += 1														

				try:
					if cadena[contador] == "*":										
						estados = self.prueba1(cadena[contador - 1], qinicial, qfinal)						
						contador += 1
				except IndexError:
				
					contador += 1
					break
					
				try:
					if cadena[contador] == "+":						
						estados = self.prueba2(cadena[contador - 1], qinicial, qfinal)						                             
						contador += 1			
				except IndexError:
				
					contador += 1
					break
													
			try:
				if cadena[contador] == "|":				
				
					#se genera una particion en la cadena					
					parte1 = cadena[:contador]							
					parte2 = cadena[contador + 1:]										
					#la parte1 ya esta resuelta, se resuelve la parte2, entonces llamamos a la función leercadena														
					estados1 = self.leercadena(parte2)																							
					estados = self.barra2(inicial, qfinal, estados1[0], estados1[1] )							
					inicial = estados[0]
					qfinal = estados[1]		
					contador += estados1[2] + 1		
			except IndexError:
			
				break

			try: 
			
				if cadena[contador] == "(":

					subcadena = ""
					aux = contador
					abrir = 0
					cerrar = 0
					while cerrar < abrir + 1:						
						aux += 1
						if cadena[aux] == "(":
							abrir += 1
						if cadena[aux] == ")":
							cerrar += 1			
							if cerrar == abrir + 1:
								break		
						subcadena += cadena[aux]																												
					estados = self.leercadena(subcadena) 																											
					if contador == 0:
						inicial = estados[0]
					else:
						qinicial1 = estados[0]
					qfinal1 = estados[1]						
					contador = aux + 1							
					try:
						self.concatenacion3(qfinal, qinicial1)						
					except UnboundLocalError:
						pass

					try:
						if cadena[contador] == "*":		
							try:							
								estados = self.clausura2(qfinal, qinicial1, qfinal1)															
								qinicial = estados[0]							
								qfinal = estados[1]
								contador += 1
							except UnboundLocalError:
								try:
									qfinal  = estados[1]
									estados = self.clausura2(qfinal, inicial, qfinal1)															
									qinicial = estados[0]							
									qfinal = estados[1]
									contador += 1					
								except UnboundLocalError:
									qfinal  = estados[1]
									estados = self.clausura2(qfinal, qinicial1, qfinal1)															
									qinicial = estados[0]							
									qfinal = estados[1]
									contador += 1					

						elif cadena[contador] == "+":
							try:
								estados = self.suma2(qfinal, qinicial1, qfinal1)
								qinicial = estados[0]
								qfinal = estados[1]
								contador += 1
							except UnboundLocalError:
								try:
									qfinal  = estados[1]
									estados = self.suma2(qfinal, inicial, qfinal1)
									qinicial = estados[0]
									qfinal = estados[1]
									contador += 1	
								except UnboundLocalError:
									qfinal  = estados[1]
									estados = self.suma2(qfinal, qinicial1, qfinal1)
									qinicial = estados[0]
									qfinal = estados[1]
									contador += 1									
						else:
							qfinal = estados[1]
					except IndexError:																	
						break

								
			except IndexError:
				pass		
		try:			
			if contador >= len(cadena):										
				return inicial, qfinal, contador	
		except UnboundLocalError:
			try:
				if contador >= len(cadena):											
					return qinicial, qfinal, contador			
			except UnboundLocalError:
				if contador >= len(cadena):											
					return inicial, qfinal1, contador	
				



	def Alcanzar(self, estadoi, letra):

		if (estadoi, letra) in self.transiciones:			
			for q in self.transiciones[(estadoi, letra)]:
				self.alcanzar.append(q)
				self.Alcanzar(q, "vacio")						
		else:
			pass



	def generar_estados(self, conjunto_estados, alf):		
		for q in conjunto_estados:						
			for letra in alf:
				self.Alcanzar(q, letra)												
				if self.alcanzar == []:
					pass
				else:					
					if conjunto_estados in self.estados_generales:
						s = "q" + str( self.estados_generales.index(conjunto_estados) )
					else:
						self.estados_generales.append(conjunto_estados)
						s = "q" + str( self.estados_generales.index(conjunto_estados) )										

					if self.alcanzar in self.estados_generales:
						t = "q" + str( self.estados_generales.index(self.alcanzar) )
					else:
						self.estados_generales.append(self.alcanzar)
						t = "q" + str( self.estados_generales.index(self.alcanzar) )	

					try:
						if self.trans[(s, letra)] == t:							
							self.alcanzar = []						
							break												
					except KeyError:

						self.trans[(s, letra)] = t
						aux = self.alcanzar
						self.alcanzar = []
						self.generar_estados(aux, alf)

						
				

	def convertir(self, cadena):

		#se obtiene el alfabeto de la expresion regular
		alfabeto = []
		for x in cadena:
			if x in alfanumerico:
				if x in alfabeto:
					pass
				else:
					alfabeto.append(x)
				
		
		
		#se llama a la funcion leercadena para que modifique el diccionario y se analicen sus transiciones
		es = self.leercadena(cadena)
		#se crea el estado inicial		
		self.Alcanzar( es[0], "vacio" )
		estado_inicial = self.alcanzar				
		estado_inicial.append(es[0])		
		self.alcanzar = []			
		#se llama a la funcion generadora de estados		
		self.generar_estados( estado_inicial , alfabeto )				
		conjunto_aceptacion = []
		for claves, valores in self.trans.items():
			for estados_finales in self.estados_generales:
				if es[1] in estados_finales:
					s = "q" + str( self.estados_generales.index(estados_finales))					
					if valores == s:
						conjunto_aceptacion.append(valores)
		
		return self.trans, conjunto_aceptacion, es[0]


def grafica(diccionario, conjunto_aceptacion):

	gautomata = Digraph(comment='grafo del automata')

	for claves, valores in diccionario.items():
		if valores in conjunto_aceptacion:											
			gautomata.attr('node', shape='doublecircle')
			gautomata.node(valores)		
		else:
			gautomata.attr('node', shape='circle')
			gautomata.node(valores)		
			gautomata.node(claves[0])		
		gautomata.edge(claves[0], valores, claves[1])		


	g= Graph(format='png')
	gautomata.format = 'png'
	gautomata.render()	


		

	gautomata = Digraph(comment='grafo del automata')

	for claves, valores in diccionario.items():
		if valores in conjunto_aceptacion:											
			gautomata.attr('node', shape='doublecircle')		
			gautomata.node(valores)		
			gautomata.attr('node', shape='circle')
		else:
			gautomata.attr('node', shape='circle')
			gautomata.node(valores)		
			gautomata.node(claves[0])		
		gautomata.edge(claves[0], valores, claves[1])		

		

def verificar(cadena):
	estado = True
	contador = 0
	if len(cadena) == "":
		estado = False
		return estado
	else:
		#se eliminan casos particulares
		if cadena[0] == "|" or cadena[0] == "+" or cadena[0] == "*":
			return False
		if "()" in cadena:
			return False
		if cadena.count("(") != cadena.count(")"):
			return False
		if cadena.count(" ") > 0:
			return False
		while contador < len(cadena):
			if cadena[contador] in alfanumerico:
				try:
					if cadena[contador + 1] == "*":
						try:
							if cadena[contador + 2] == "*" or cadena[contador + 2] == "+":
								return False
						except IndexError:
							pass
						contador += 2
				
					elif cadena[contador + 1] == "+":
						try:
							if cadena[contador + 2] == "*" or cadena[contador + 2] == "+":
								return False
						except IndexError:
							pass
						contador += 2		

					else:
						contador += 1				
				except IndexError:
					return True
			
			try:
				if cadena[contador] == "|":
					parte1 = cadena[:contador]
					parte2 = cadena[contador + 1:]					
					estado1 = verificar(parte2)					
					if estado == True and estado1 == True:
						contador += len(parte2)
						return True
					else:
						return False
				
					
			except IndexError:
				return True

			try:
				if cadena[contador] == "(":

					subcadena = ""
					aux = contador
					abrir = 0
					cerrar = 0
					while cerrar < abrir + 1:						
						aux += 1
						if cadena[aux] == "(":
							abrir += 1
						if cadena[aux] == ")":
							cerrar += 1			
							if cerrar == abrir + 1:
								break		
						subcadena += cadena[aux]															
					contador = aux				
					estado2 = verificar(subcadena)					
					if estado == True and estado2 == True:						
						#aqui se verifica si despues del parentesis hay otro operador
						try:
							if cadena[contador + 1] == "*":
								contador += 2
							elif cadena[contador + 1] == "+":
								contador += 2
							else:
								contador += 1
						except IndexError:
							return True
					else:
						return False

			except IndexError:
				return True
			
	
	if contador == len(cadena):
		return True



def expresiones(request):
	objetos = Regex.objects.all()
	lista = []
	for objeto in objetos:
		lista.append(objeto.regex)
		
	form = regexform(request.POST)
	if request.method == 'POST':
		if request.POST['regex'] in lista:
			expresionR = Algoritmo()
			eR = expresionR.convertir(request.POST['regex'])
			grafica(eR[0], eR[1])

		if form.is_valid():						
			if verificar( request.POST['regex']) == True:				
				form.save()
				expresionR = Algoritmo()
				eR = expresionR.convertir(request.POST['regex'])
				grafica(eR[0], eR[1])
			else:
				return HttpResponse("La expresión ingresada es inválida, para mas ayuda puede consultar la gramática de las expresiones. Además no se aceptan espacios vacios")
	return render( request, 'regex/expresiones.html', {'form': form})


def gramatica(request):
    return render(request, 'regex/gramatica.html')


