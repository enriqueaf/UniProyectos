# -*- coding: UTF-8 -*-
import socket,signal
conseguido = []
s = socket.socket()
s.connect(("192.168.1.8", 2869))
a = raw_input('Nombre >> ')
s.send(a)
recibido = s.recv(1024)
s.send('OK')
s.settimeout(65)
def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(0)

recibido = recibido.split(',')
inc = recibido[3]
inc = inc.split(';')
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
		signal.alarm(65)	
		try:
			mensaje = raw_input("> ")
			s.send(mensaje)
			signal.alarm(0)
		except IOError: 
			print 'sorry'
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
