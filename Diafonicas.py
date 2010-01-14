def Diafonicas(n):
 dif = []
 x = n
 i = 0
 while x != (n/2 - 1 + (n%2)):
  dif.append([x,i])
  i = 1 + i
  x = n - i
 return dif
a = input('Introduce un numero: ')
print Diafonicas(a)
