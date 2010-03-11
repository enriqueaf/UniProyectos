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
while True:
	recibido = s.recv(1024)
	print "Recibido:", recibido
	recibido = recibido.split(',')
	if recibido[0] == 'DI':
		mensaje = raw_input("> ")
		s.send(mensaje)
	elif recibido[0] == 'LETRA':
		nume = recibido[2].split(';')
		for i in nume:
			conseguido[int(i)]=recibido[1]
		print conseguido
		s.send('OK')


	else: 
		s.send('OK')

print "adios"
s.close()
