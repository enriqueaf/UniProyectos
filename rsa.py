# -*- coding: utf-8 -*-
import sys
def descifrar(m,x,n,d):
 md = ''
 for i in m:
  md = md + d[exponenciar(x,int(i),n)]
 return md

def exponenciar(x,y,n=0):
 bi = y
 zi = 1
 di = []
 i = x
 while i != 0:
  di.append(i%2)
  i = i/2
 for i in di:
  zi = zi * bi ** i % n
  bi = bi**2%n
 return zi

print 'Bienvenido a la exponenciación rápida'
if len(sys.argv) != 2:
  print '¿Diga los números?(mensaje(,)/j/modulo'
  e = raw_input('>>> ')
else:
  e = sys.argv[1]
e = e.split('/')
i = e[0].split(',')
diccionario = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print descifrar(i,int(e[1]),int(e[2]),diccionario)
