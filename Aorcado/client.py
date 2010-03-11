# -*- coding: UTF-8 -*-
import socket
conseguido = []
s = socket.socket()
s.connect(("localhost", 9999))
a = raw_input('Nombre >> ')
s.send(a)
recibido = s.recv(1024)
s.send('OK')
recibido = recibido.split(',')
inc = recibido[3]
for i in inc:
	print int(i)*'_',
	for n in range(int(i)):
		conseguido.append('_')
	conseguido.append(' ')
print 
err = [' ','Sólo 1 letra','Letra ya introducida']
while True:
	recibido = s.recv(1024)
	print "Recibido:", recibido
	recibido = recibido.split(',')
	if recibido[0] == 'DI':
		mensaje = raw_input("> ")
		s.send(mensaje)
	elif recibido[0] == 'LETRA':
		nume = recibido[2].split(';')
		if nume[0] == '-1':
			print 'La letra:',recibido[1],'no exta'
		else: 
			for i in nume:
				conseguido[int(i)]=recibido[1]
			T = ''
			for i in conseguido:
				T +=i
			print T
		s.send('OK')

	elif recibido[0] == 'ERROR':
		print err[int(recibido[1])]
		s.send('OK')
	elif recibido[0] == 'FIN':
		print 'GANO',recibido[1]
		s.send('OK')
		break
	else: 
		s.send('OK')

print "adios"
s.close()
