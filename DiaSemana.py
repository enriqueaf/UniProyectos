# -*- coding: utf-8 -*-
from datetime import date
import sys
print 'Bienvenido a la busqueda del día'
print '---------------------- ************ ------------------------'
Semana = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
if len(sys.argv) != 2:
  print '¿Dime un día del tipo dd/mm/yyyy?'
  ## En e se guarda la entrada por teclado
  e = raw_input('>>> ')
else:
  e = sys.argv[1]

a = e.split('/')
print 'El',e,'coincide con',Semana[date(int(a[2]),int(a[1]),int(a[0])).weekday()]
