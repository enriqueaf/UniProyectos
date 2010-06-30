class MatrizIncidencia:
    def __init__(self,lista):
        self._lista = lista
        self.vertices = len(lista)-1

    def estan_unidos(self,a,b):
        if self._lista[a][b]==1: return True
        return False
def pintar(n,M):
    pintura = coloreando(0,M,[])
    if n in pintura: return False
    return pintura
def coloreando(V,M,Colors):
    temp = []
    for i in range(V):
        if M.estan_unidos(i,V): temp.append(Colors[i])
    entro = False
    a = 0
    while not(entro):
        if not(a in temp) and not(entro):
            Colors.append(a)
            entro = True
        a += 1
    if V == M.vertices: return Colors
    else: return coloreando(V+1,M,Colors)

def main():
    R = [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
    S = MatrizIncidencia(R)
    print pintar(10,S)
if __name__=='__main__':
    main()
