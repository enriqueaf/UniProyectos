import random
from math import sqrt,log
class Tabla:
	def __init__(self,n):
		self._tabla = list(n)

	def VerTabla(self):
		return self._tabla

	def VerLongitud(self):
		return len(self._tabla)

	def CambiarTabla(self,n):
		self._tabla = list(n)


class TablaAleatoria(Tabla):
	def __init__(self,x,y):
		self._tabla = []
		self._longitud = int(x)
		self._maximo = int(y)
		self.__GTabla()

	def __GTabla(self):
		for i in range(self._longitud):
			self._tabla.append(random.randint(1,self._maximo))
	def VerMaximo(self):
		return self._maximo()
	def CambiarTabla(self,n):
		self.Regenerar()
	def CambiarLongitud(self,n):
		self._longitud = int(n)
		return self.Regenerar()
	
	def CambiarMaximo(self,n):
		self._maximo = int(n)
		return self.Regenerar()

	def CambiarMaximoYLongitud(self,x,y):
		self._longitud = int(x)
		self._maximo = int(y)
		return self.Regenerar()
	
	def Regenerar(self):
		self._tabla = []
		self.__GTabla()
		return self._tabla

class Operaciones(object):
	" Genero tablas y saco datos sobre ellas "
	def __init__(self,tabla):
		self._tabla = tabla

	def __str__(self):
		a = 'La Tabla: ' + str(self._tabla.VerTabla()) + '\n'
		a += 'Media: ' + str(self.HacerMedia()) + '\n'
		a += 'Desviacion: ' + str(self.HacerDesviacion()) + '\n'
		a += 'Cuadrados Perfectos: ' + str(self.VerCuadradosPerfectos()) + '\n'
		a += 'Pares: ' + str(self.VerPares()) + '\n'
		a += 'Numeros con log base 2 menores que 2 : ' + str(self.VerLog2MenoresQue(2)) + '\n'		
		a += 'Esta Ordenada de Menor a Mayor?: ' + str(self.EstaOrdenada()) + '\n'
		a += 'Picos: ' +str(self.VerPicos()) + '\n'
		a += 'Potencias de Dos' + str(self.VerPotenciasDeDos()) +'\n'
		a += 'Es Polindroma?: ' + str(self.EsPolindroma()) + '\n'
		a += 'Primos: ' + str(self.VerPrimos()) + '\n'
		a += 'Sumas: ' +str(self.VerSumasParciales()) + '\n'
		return a

	


	def HacerMedia(self):
		contador = 0
		for i in self._tabla.VerTabla():
			contador = i + contador
		return contador/self._tabla.VerLongitud()

	def HacerVarianza(self):
		contador = 0
		for i in self._tabla.VerTabla():
			contador =  i**2 + contador
		return (1.0/self._tabla.VerLongitud())*contador - self.HacerMedia()**2
	
	def HacerDesviacion(self):
		return sqrt(self.HacerVarianza())

	def VerCuadradosPerfectos(self):
		contador = []
		for i in self._tabla.VerTabla():
			if i % sqrt(i) == 0.0 and i != 1:
				contador.append(i)
		return contador

	def VerPares(self):
		contador = []
		for i in self._tabla.VerTabla():
			if i % 2 == 0:
				contador.append(i)
		return contador


	def VerLog2MenoresQue(self,n):
		contador = []
		for i in self._tabla.VerTabla():
			if n > log(i,2):
				contador.append(i)
		return contador
	def VerPicos(self):
		contador = []
		for i in range(1,self._tabla.VerLongitud()-1):
			if (self._tabla.VerTabla()[i-1] < self._tabla.VerTabla()[i]) and (self._tabla.VerTabla()[i+1] < self._tabla.VerTabla()[i]):
				contador.append(self._tabla.VerTabla()[i])
		return contador

	def EstaOrdenada(self,reverse = False):
		for i in range(self._tabla.VerLongitud()-1):
			if (self._tabla.VerTabla()[i] < self._tabla.VerTabla()[i+1]) == reverse:
				return False
		return True
	def _PDDos(self,n):
		if (n%2 == 0) and (n/2 == 1):
			return True
		elif n%2 == 0:
			return self._PDDos(n/2)
		else:
			return False
	def EsPolindroma(self):
		for i in range(int(self._tabla.VerLongitud()/2)):
			if self._tabla.VerTabla()[i] != self._tabla.VerTabla()[(-1)*(i+1)]:
				return False
		return True

	def VerPotenciasDeDos(self):
		contador = []
		for i in self._tabla.VerTabla():
			if self._PDDos(i):
				contador.append(i)
		return contador
	def _EsPrimo(self,n):
		for i in range(2,(int(sqrt(n)+1))):
			if n%i == 0:
				return False
		return True

	def VerPrimos(self):
		contador = []
		for i in self._tabla.VerTabla():
			if self._EsPrimo(i):
				contador.append(i)
		return contador
	def VerSumasParciales(self):
		sumas = []
		for i in range(self._tabla.VerLongitud()):
			contador = 0
			for a in range(i+1):
				contador += self._tabla.VerTabla()[a]
			sumas.append(contador)
		return sumas

				

if __name__ == "__main__":
	t = TablaAleatoria(10,50)
	o = Operaciones(t)
	print o
	t.Regenerar()
	print o
	t.CambiarLongitud(80)
	print o
