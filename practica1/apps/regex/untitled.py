
from graphviz import Digraph, Graph
alfanumerico = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

class Algoritmo:
	
	def __init__(self):
		
		self.transiciones = {}
		self.contador = [0]
		self.alfanumerico =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
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
					print(estados)
					qinicial = estados[0]
					inicial = estados[0]
					qfinal = estados[1]	
					contador += 1					
				else:
					estados = self.concatenacion2( cadena[contador], qfinal )	
					qinicial = estados[0]				
					qfinal = estados[1]	
					print(qfinal)
					contador += 1
					print(estados)
				try:
					if cadena[contador] == "*":										
						estados = self.prueba1(cadena[contador - 1], qinicial, qfinal)						
						contador += 1
				except IndexError:
					print("cadena terminada")
					contador += 1
					break
					
				try:
					if cadena[contador] == "+":						
						estados = self.prueba2(cadena[contador - 1], qinicial, qfinal)						                             
						contador += 1			
				except IndexError:
					print("cadena terminada")
					contador += 1
					break
													
			try:
				if cadena[contador] == "|":				
				
					#se genera una particion en la cadena					
					parte1 = cadena[:contador]							
					parte2 = cadena[contador + 1:]		
					print(parte1, parte2)				
					#la parte1 ya esta resuelta, se resuelve la parte2, entonces llamamos a la función leercadena
					estados1 = self.leercadena(parte2)		
					print(estados1)									
					estados = self.barra2(inicial, qfinal, estados1[0], estados1[1] )							
					inicial = estados[0]
					qfinal = estados[1]		
					contador += estados1[2] + 1		
			except IndexError:
				print("la cadena o subcadena se ha leido")			
				break

			try: 
			
				if cadena[contador] == "(":

					subcadena = ""
					aux = contador + 1					
					temp = 0
					while cadena[aux] != ")" or temp != -1:
							
						if cadena[aux] == "(":
							temp += 1
						if cadena[aux] == ")":
							temp -= 1
						if temp == -1:
							break
						subcadena += cadena[aux]
						aux += 1

					contador = aux + 1					
					estados = self.leercadena(subcadena) 
							
					
					qinicial = estados[0]
					qfinal = estados[1]					
					try:
						if cadena[contador] == "*":								
							estados = self.clausura3(qinicial, qfinal)								
							qinicial = estados[0]
							qfinal = estados[1]
							contador += 1
					except IndexError:											
						print("Cadena Termianda")
						break

					try:
						if cadena[contador] == "+":
							estados = self.suma3(qinicial, qfinal)
							qinicial = estados[0]
							qfinal = estados[1]
							contador += 1
					except IndexError:											
						print("Cadena Termianda")
						break	
					'''else:
						qinicial = estados[0]
						print(qinicial)
						qfinal = estados[1]
						try:
							if cadena[contador] == "*":
								print(qfinal)
								estados = self.clausura2(qfinal, estados[0], estados[1])
								qfinal = estados[1]
								print(qfinal)
								contador += 1
						except IndexError:
							print("Cadena terminada")
							break
						
						try:
							if cadena[contador] == "+":						
								estados = self.suma2(qfinal, estados[0], estados[1])
								qfinal = estados[1]
								contador += 1
						except IndexError:
							print("Cadena terminada")
							break'''

					
			except IndexError:
				print("Cadena terminada")

		if contador >= len(cadena):	
			print(self.transiciones)						
			return inicial, qfinal, contador	



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
				self.Alcanzar( q, letra)
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

					if conjunto_estados == self.alcanzar:

						self.trans[(s, letra)] = t
						self.alcanzar = []

					else:
						self.trans[(s, letra)] = t
						aux = self.alcanzar
						self.alcanzar = []
						self.generar_estados(aux, alf)
						
	def convertir(self, cadena):

		#se obtiene el alfabeto de la expresion regular
		alfabeto = []
		for x in cadena:
			if x in self.alfanumerico:
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

	print(conjunto_aceptacion)
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

	g = Graph(format='png')
	gautomata.format = 'png'
	gautomata.render(view=True)		


instancia = Algoritmo()
r = instancia.convertir("(a|b)*c")
print(r)