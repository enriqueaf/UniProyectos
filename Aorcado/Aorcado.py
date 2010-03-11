# -*- coding: UTF-8 -*- 
class AorcadoFallo(Exception):
	pass

def log(n):
	print '>>',n,'<<'
#Interfaz para la clase jugador
class Jugador:
	def __init__(self,Nombre,Juego):
		self.__Juego = Juego
		self.__Juego.NuevoJugador(self)
		self.__Nombre = Nombre
	def Anuncio(self,n):
		print n
	def Error(self,n):
		print 'Error: ',n
	def Turno(self):
		return raw_input('>>> ')

	def FinTurno(self):
		print 'Fin Turno'
	
	
	def __SumarFallo(self):
		pass
	

	def ResetearContadores(self):
		self.__Intentos = 0
		self.__Fallos = 0
	
	def VerNombre(self):
		return self.__Nombre
	
	def VerFallos(self):
		pass
	def VerIntentos(self):
		pass

class Aorcado:
	__Palabra = {}
	__Conseguido = {}
	__LetrasP = []
	__Jugador=[]
	__Conseguido = {}
	__Turno=0
	__Estado=0 # 0 => ESPERANDO; 1 => EMPEZADO; 2 => FINALIZADO

	def __init__(self,Palabra=None,Pista=None,MJugadores = 5):
		log('Inicializando objeto')
		self.__MJugadores = MJugadores
		if Palabra is None: 
			Palabra, Pista = self.__ElegirPalabra()
		self.__TratarPalabra(Palabra)
		self.__Pista = Pista	
	
	def NuevoJugador(self,jugador):
		if len(self.__Jugador) > self.__MJugadores: raise AorcadoFallo('Demasiados Jugadores')
		elif self.__Jugador.count(jugador) != 0: raise AorcadoFallo('Ya exite el Jugador')
		jugador.Anuncio(['PISTA',self.__Pista,'INCOGNITAS',self.__Incognitas,'CONSEGUIDO',str(self.__Conseguido)])
		self.__Jugador.append(jugador)


	def IniciarJuego(self):
		if self.__Estado == 1: raise AorcadoFallo('El Juego ya está empeazado')
		self.__Estado = 1
		log('Iniciando el Juego con: ')
		for i in self.__Jugador: 
			log(i.VerNombre())
			i.ResetearContadores()
		self.__GlobalAnuncio(['EMPEZAR'])
		self.__Turno = 0
		self.__Jugar()
	
	def __Jugar(self):
		#Mejor opción de diseño con while??
		if self.__Conseguido == self.__Palabra:
			self.__GlobalAnuncio(['FIN',self.__Jugador[self.__Turno]])
			log('Gano el jugador '+self.__Jugador[self.__Turno].VerNombre())
		else:
			jugador = self.__Jugador[self.__Turno]
			letra = jugador.Turno() 
			log('Juega el jugador '+jugador.VerNombre()+' Con letra: '+str(letra))
			if letra == '-1': 
				self.CambiarTurno()
				self.__Jugar()
			elif len(letra) != 1:
				log('InputError 1')
				self.__Jugador[self.__Turno].Error(1)
				self.__Jugar()
			elif self.__LetrasP.count(letra):
				log('InputError 2')
				self.__Jugador[self.__Turno].Error(2)
				self.__Jugar()
			else:
				self.__LetrasP.append(letra)
				self.__BuscarLetraYSutituir(letra)
				self.__Jugar()


	def __BuscarLetraYSutituir(self,n):
		letra = n.upper()
		if letra in self.__Palabra: 
			self.__Conseguido[letra] = self.__Palabra[letra]
			a= ''
			for i in self.__Palabra[letra]:
				a += str(i)+';'
			letras = a[:-1]
		else: 
			letras='-1'
			

		self.__GlobalAnuncio(['LETRA',letra,letras])

		if letras=='-1':
			log('No se encontraron letras para: '+letra)
			self.CambiarTurno()

	def __GlobalAnuncio(self,n):
		for i in self.__Jugador: i.Anuncio(n)

	def CambiarTurno(self):
		if not(self.ChequearEstado(1)): raise AorcadoFallo('Juego aún no empezado')
		self.__Jugador[self.__Turno].FinTurno()
		self.__Turno = (self.__Turno + 1) % len(self.__Jugador)
		self.__GlobalAnuncio(['CTURNO',self.__Jugador[self.__Turno]])
		log('Cambiando turno a '+str(self.__Turno))
	
	
	def BorrarJugador(self,jugador):
		try: 
			b = self.__Jugador.index(jugador)
			self.__Jugador.remove(jugador)
		except ValueError: raise AorcadoFallo('El jugador que intenta borrar no existe')
		log('Borrado del juego al jugador: '+jugador.VerNombre())
		if b < self.__Turno:
			self.__Turno = self.__Turno - 1


	def ChequearEstado(self,AComprobar = None):
		log('Comprobando estado: '+str(self.__Estado))
		if AComprobar is None: return self.__Estado
		elif self.__Estado == AComprobar: return True
		else: return False

	def ChequearTurno(self):
		log('Comprobando el turno '+self.__Turno)
		return self.__Jugador[self.__Turno]
	
	def __TratarPalabra(self,Palabra):
		self.__Palabra = {}
		Palabra2 = list(Palabra.upper())
		Palabra1 = set(Palabra.upper())
		try: Palabra1.remove(' ')
		except: log('No espacios')
		for i in Palabra1:
			self.__Palabra[i] = []
			while Palabra2.count(i) != 0:
				self.__Palabra[i].append(Palabra2.index(i))
				Palabra2[Palabra2.index(i)] = -1
		log('Palabra '+Palabra+' '+str(self.__Palabra))
		Pa = Palabra.split(' ')
		self.__Incognitas = ''
		for i in Pa:
			self.__Incognitas += str(len(i))
		log('Incognitas '+self.__Incognitas)	

	
	def VerConseguido(self):
		return self.__Conseguido
	def VerPista(self):
		return self.__Pista

	def VerPalabra(self,seguro=False):
		if seguro or not(self.ChequearEstado()): 
			self.__Fallos = self.__MFallos
			return self.__Palabra
		else: return False
	
if __name__ == '__main__':
	Juego = Aorcado('Eres Un Capullo','UPPS')
	Jugador('Enrique',Juego)
	Jugador('MyPlayer',Juego)
	Jugador('Waldo',Juego)
	Juego.IniciarJuego()
