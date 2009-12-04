# -*- coding: utf-8 -*-
import time,sys

def Factores(n):
  f = []
  c = []
  for i in range(2,n):
    if n%i == 0:
      #c = Factores(i)
      f.extend(Factores(i))
      f.extend(Factores(n/i))
      break
  if len(f) == 0:
    return [n]
  else:
    return f
def Repes(f):
    sim = set(f)
    multi = {}
    for i in sim:
      multi[i] = f.count(i)
    return multi

print 'Bienvenido a la factorizacion'
if len(sys.argv) != 2:
  print '¿Hasta que número desea factorizar?'
  e = int(raw_input('>>> '))
else:
  e = int(sys.argv[1])
c = 0
start = time.time()
for i in range(2,e+1):
  f = Factores(i)
  if len(f) == 1:
    print '|--------->',i,' es primo ',c
    c = 0
  else:
    multi = Repes(f)
    a = '['
    for s in multi:
      a += str(s)+'^'+str(multi[s])+','
    a = a[:-1] + ']'
    print 'Factores de ',i,' son: ',a
    c += 1
print time.time()-start
