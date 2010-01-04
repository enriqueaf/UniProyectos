# -*- coding: utf-8 -*-
import sys
def mcd(x,y,q):
 r = x%y
 q.extend(str(x/y))
 if r != 0:
  return mcd(y,r,q)
 else:
  return y,q

def Bezout(q):
 x = [[1,0],[0,1]]
 for i in [0,1]:
  for s in range(len(q)):
   t = x[i][1]
   x[i][1] = x[i][0] - x[i][1]*int(q[s])
   x[i][0] = t
 return [x[0][0],x[1][0]]

print 'Bienvenido al mcdeitor'
if len(sys.argv) != 2:
  print '¿Digame los números?'
  e = raw_input('>>> ')
else:
  e = sys.argv[1]
e = e.split(' ')
i = mcd(int(e[0]),int(e[1]),[])
print i[0]
b = Bezout(i[1])
print e[0],'*',b[0],' + ',e[1],'*',b[1], ' = ' , int(e[0])*b[0]+int(e[1])*b[1]
