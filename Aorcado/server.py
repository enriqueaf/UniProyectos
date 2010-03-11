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
	def Anuncio(self,n):
		an = ''
		print 'Enviando',n
		for i in n:
			an += str(i)+','
		print an[:-1]
		self.__Conexion[0].send(an[:-1])
		self.__Cheq()

	def __Cheq(self):
		self.__TimeO()
		#r = self.__Conexion[0].recv(1024)
		try: r = self.__Conexion[0].recv(1024)
		except: r = '-1'
		self.__TimeO()
		if r.upper() != 'OK':
			self.__Conexion[0].close()
			self.__Juego.BorrarJugador(self)
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
		return self.__Conexion[0].recv(1024)

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)
s.settimeout(5)
Juego = Aorcado.Aorcado('ERES UN CAPULLO','¿¿COMO ERES??')
while True:
	try: sc, addr = s.accept()
	except: break
	nombre = sc.recv(1024)
	JugadorC(nombre,Juego,[sc,addr])
Juego.IniciarJuego()
	


print "adios"
s.close()
