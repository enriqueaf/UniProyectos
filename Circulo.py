from math import sqrt
def distancia(x,y):
 return sqrt(x**2+y**2)
def Circulo(r):
 for y in range(2*r):
  for x in range(2*r):
   if distancia(r-x,r-y) <= r-1:
    print '*',
   else:
    print ' ',
  print

print 'Introuzca un numero'
a = input('>>> ')
Circulo(a)
