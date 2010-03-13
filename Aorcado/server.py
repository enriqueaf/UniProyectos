# -*- coding: UTF-8 -*- 
import socket,Aorcado
class JugadorC(Aorcado.Jugador):
	__Time=False
	def __init__(self,nombre,juego,conex):
		self.__Nombre = nombre
		self.__Juego = juego
		self.__Conexion = conex
		juego.NuevoJugador(self)
		print conex
	def Error(self,n):
		self.__Conexion[0].send('ERROR,'+str(n))
		self.__Cheq()
	def Anuncio(self,n):
		an = ''
		if n[0] == 'FIN':
			T = n[1].VerNombre()
			an = 'FIN,'+T
		else:
			for i in n:
				an += str(i)+','
			an = an[:-1]
			print 'Enviando',an
		self.__Conexion[0].send(an)
		self.__Cheq()

	def __Cheq(self):
		self.__TimeO()
		#r = self.__Conexion[0].recv(1024)
		try: r = self.__Conexion[0].recv(1024)
		except: r = '-1'
		self.__Conexion[0].settimeout(10)
		if r.upper() != 'OK':
			self.__Conexion[0].close()
			self.__Juego.BorrarJugador(self)
		else: self.__Conexion[0].settimeout(60)
	def __TimeO(self):
		if self.__Time:
			self.__Conexion[0].settimeout(10)
			self.__Time= False
		else: 
			self.__Conexion[0].settimeout(60)
			self.__Time = True

	def VerNombre(self):
		return self.__Nombre
	def Turno(self):
		self.__Conexion[0].send('TURNO')
		self.__Cheq()
		self.__Conexion[0].send('DI')
		try: a = self.__Conexion[0].recv(1024)
		except: 
			self.__Juego.CambiarTurno()
		return a

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)
s.settimeout(80)
Juego = Aorcado.Aorcado('SOYS TODOS UNOS ESTUPIDOS','¿¿COMO ERES??')
while True:
	try: sc, addr = s.accept()
	except: break
	print 'Nuevo Usuario conectado',addr
	nombre = sc.recv(1024)
	JugadorC(nombre,Juego,[sc,addr])

try: Juego.IniciarJuego()
except: print 'Intento de empezar pero no hay jugadores'
	


print "adios"
s.close()
