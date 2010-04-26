import logging
from copy import deepcopy
from time import sleep
class JuegoDeLaVida(Exception):
    pass
class World:
    '''
    In this world, the people, as in any other, are reproduce and die.
    For live they have to be with two partners or one.
    For reproduce there must be three
    Args:
        - board: list
        - stop*: Boolean
        - die*: list => int (1..8)
        - reproduce*: list => int (1..8)
    '''
    _stop = False
    _die = [0,1,4,5,6,7,8]
    _repr = [3]
    def __init__(self,board,args = {}):
        if len(args) >= 1:
            if args.has_key('stop'): self._stop = args['stop']
            if args.has_key('die'): self._die = deepcopy(args['die'])
            if args.has_key('repr'): self._repr = deepcopy(args['repr'])
            if args.has_key('sleep'): self._sleep = int(args['sleep'])
        self._sizes = [len(board),len(board[0])]
        if not World.valid_board(board): raise JuegoDeLaVida('Not valid board')
        self._board = deepcopy(board)
        self._create_log()
        self.log.info('Juego de la vida creado')
    
    def _create_log(self):
        self.log = logging.getLogger('JuegoDeLaVida')
   
    def _reproduce(self,x,y):
        self.log.info('Creando una nueva celula en: '+str(x)+','+str(y))
        x,y = int(x),int(y)
        self._board[y][x] = 1
    def _kill(self,x,y):
        x,y = int(x),int(y)
        self.log.info('Matando una celula en: '+str(x)+','+str(y))
        self._board[y][x] = 0
    def evolution(self):
        while True:
            CopyBoard = deepcopy(self._board)
            self.log.info('Evolucionando a las celula')
            self.log.debug('Tablero:'+str(self._board))
            self._check_neighbourds()
            
            for repr in self._repr:
                for i in self._neighbourds[repr]:
                    self._reproduce(i[0],i[1])
            for die in self._die:
                for i in self._neighbourds[die]:
                    if self._board[i[1]][i[0]] == 1: self._kill(i[0],i[1])

            if self._stop: break
            if CopyBoard == self._board: 
                self.log.info('Se empieza a reptir')
                break
            print self
            self._for_next()
        
    def _for_next(self):
        sleep(self._sleep)

    def _check_neighbourds(self):
        moves = [[0,1],[1,1],[1,-1],[1,0],[0,-1],[-1,-1],[-1,1],[-1,0]]
        self._neighbourds = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        for y in range(self._sizes[0]):
            for x in range(self._sizes[1]):
                neigh = 0
                for m in moves:
                    cy,cx = y+m[1],x+m[0]
                    if 0 <= cy < self._sizes[0] and 0 <= cx < self._sizes[1]:
                        if self._board[cy][cx] == 1: 
                            neigh += 1
                            self.log.debug('Por ahora '+str(x)+','+str(y)+' tiene '+str(neigh))
                self._neighbourds[neigh].append([x,y])
        self.log.debug('Neighbourds: '+str(self._neighbourds))


        

    def __str__(self):
        text =' '
        for i in range(self._sizes[1]):
            text = text+' '+str(i) 
        text = text+'\n'
        for i in range(self._sizes[0]):
            text =text+str(i)
            for a in range(self._sizes[1]):
                if self._board[i][a] == 1: text =text+' #'
                else: text=text+' .'
            text =text+'\n'
        return text

        
        

    '''
    Check if the dimensions are all the same, and if it has 0's and 1's only.
    <= boolean
    '''

    @staticmethod
    def valid_board(board):
        board = deepcopy(board)
        size = len(board[0])
        for i in board:
            if len(i)!= size: 
                logging.debug('No es valido por diferentes tamanos')
                return False
            for a in i:
                if a != 1 and a != 0: 
                    logging.debug("No 0's o 1's")
                    return False
        return True
    @classmethod
    def from_keyboard():
        pass
    @classmethod
    def from_file(url):
        pass

def main():
    LOG_FILENAME = '/var/tmp/JuegoDeLaVida.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
    table = [0]*10
    tablero = [deepcopy(table),deepcopy(table),deepcopy(table),deepcopy(table),deepcopy(table),deepcopy(table),deepcopy(table),deepcopy(table),deepcopy(table),deepcopy(table)]
    tablero[2][3],tablero[2][4],tablero[2][5],tablero[3][5],tablero[1][5] = 1,1,1,1,1
    mundo = World(tablero,{'stop':False,'sleep':0.5})
    mundo.evolution()
if __name__=="__main__":
    main()
