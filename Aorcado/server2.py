# -*- coding: UTF-8 -*- 
import socket
s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)
s.settimeout(80)
sc, addr = s.accept()
print 'Nuevo Usuario conectado',addr
algo = sc.recv(1024)
print algo
b = ''
while True:
	a = raw_input('>>> ')
	sc.send(a)
	if a.upper() == 'N':
		break
	print 'Enviando',a
	reci = sc.recv(1024)
	print 'Recibido',reci

print "adios"
s.close()
