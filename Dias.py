# -+- coding: utf-8 -+-
# Esto lo vi en internet como una manera de saber el día de la semana, pero no se yo si está bien.
import time
def diasSemana(DiaNum = -1):
	dias=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
	if DiaNum==-1:
		import time
		laFecha=time.localtime(time,time())
		DiaNum=laFecha[6]
	return dias[DiaNum]
print diasSemana(-1)
