# -*- coding: utf-8 -*-
#Defino la funcion
import sys
from math import sqrt
def esPrimo(n):
  ## Preparo un bucle para los numeros de [2,n-1]
  for i in range(2,(int(sqrt(n)+1))):
    if n%i == 0:
  #    print n, 'NO es primo'
      ## Si en algun momento se es cierta esta sentencia signfica no es primo
      ## El return me sirve para terminar el bucle
      return False
  ## Si llega hasta aqui significa que ningún numero del bulce es divisro de n
  print n, 'es primo'
  return True

if len(sys.argv) != 2:
  print 'Bienvenido al investigador de primos'
  print '¿Hasta que numero?'
  ## En e se guarda la entrada por teclado
  e = int(raw_input('>>> '))
else:
  e = int(sys.argv[1])

for i in range(2,e+1):
    esPrimo(i)
