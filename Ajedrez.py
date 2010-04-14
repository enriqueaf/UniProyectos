# -*- coding: UTF-8 -*-

# Enrique Álvarez Fernandez
# 04/2010
# GPL
#######################################################
import random
from math import sqrt
from logging import *
'''
TODO: Implementar un buen sistema de logging, con el paquete logging de python.

Para conseguir el objetivo de crear un ajedrez, se van a construir dos interfaces: Una para el los jugadores y otra para las fichas.
Se construiran dos nuevos tipos: Postion and Move
Después estás serán implementadas de forma que sea sencillo poder crear un caballo, un alfil o lo quesea, situando la parte pensante dentro de la clases tipo jugador.
La clase Tablero, se encagara de manejar las piezas y movimientos, verificando su valided.
'''
LETRAS = ['A','B','C','D','E','F','G','H']
def convert_letter_to_number(a):
    for e in range(len(c)):
        for i in range(len(LETRAS)):
            if LETRAS[i] == c[e][0].upper():
                c[e] = str(i)+c[e][1]
                break
class AjedrezError(Exception):
    '''
    Tipo de error que se ejecutara, cuando halla un problema dentro del propio tablero.
    '''
    pass
class NextTurn(Exception):
    pass
class JuegoFinalizar(Exception):
    pass
class JuegoError(Exception):
    pass
# ----------------------------------------------------------------------
class Position(object):
    '''
    Type position para las posiciones
    TODO: Position - Position = Move
    '''
    def __init__(self,x,y):
        self.X = int(x)
        self.Y = int(y)
    def __repr__(self):
        return 'X:'+str(self.X)+' Y:'+str(self.Y)
    def __eq__(self,other):
        if type(other)== Position:
            return other.X == self.X and other.Y == self.Y
        else:
            raise AjedrezError('Comparacion de objetos diferentes')
    def __sub__(self,other):
        return Move(self.X-other.X,self.Y-other.Y)
    def __hash__(self):
        return self.X*50565+self.Y*41561556
    def __len__(self):
        return 1
    def __add__(self,other):
        if type(other) == Move:
            return Position(self.X + other.X,self.Y + other.Y)
        elif type(other) == Vector:
            return PositionVector(self.X,self.Y,other)
        else:
            raise AjedrezError('Itentando sumar type: Position con otro diferente a type: Move')
class PositionVector(object):
    def __init__(self,x,y,vector):
        self.X = int(x)
        self.Y = int(y)
        self.Vector = vector
        self.a = 0
    def __iter__(self):
        return PositionVector(self.X,self.Y,self.Vector)
    def __len__(self):
        return 2
    def next(self):
        self.a +=1
        return Position(self.a * self.Vector.X + self.X, self.a * self.Vector.Y + self.Y)
        
class Vector(object):
    def __init__(self,x,y):
        if x == 0 and y == 0:
            AjedrezError('Vector no valido')
        self.X = int(x)
        self.Y = int(y)
    def __eq__(self,other):
        if type(other) == Move:
            if self.X == 0:
                return other.X == 0 and other.Y%self.Y == 0
            elif self.Y == 0:
                return other.Y == 0 and other.X%self.X == 0
            return other.X/self.X == other.Y/self.Y
        else:
            raise AjedrezError('No move')
class Move(object):
    '''
    Type Move para los movimientos
    '''
    def __init__(self,x,y):
        self.X = int(x)
        self.Y = int(y)
    def __str__(self):
        return 'X:'+str(self.X)+' Y:'+str(self.Y)
    def __len__(self):
        print self
        a = sqrt((self.X**2)+(self.Y**2))
        print a
        return a

    def __add__(self,other):
        if type(other) == Move:
            return Move(self.X+other.X,self.Y+other.Y)
        elif type(other) == Vector:
            return other == self
        else:
            raise AjedrezError('Intentando sumar type: Move con otro NO type: Move')
    def __eq__(self,other):
        return self.X == other.X and self.Y == other.Y
    def __repr__(self):
        return 'X:'+str(self.X)+' Y:'+str(self.Y)
    def __hash__(self):
        return str(self.X)+';'+(self.Y)
# ------------------------------------------------------------------------
class Player:
    '''
    Interfaz para los jugadores
    '''
    def get_situation(self):
        return self._situation
    def get_turn(self):
        pass
    def lost_turn(self):
        pass
    def notify_event(self,type,msg):
        '''
        Por ahora no la he utilizado, pero debería de advertir a los usuarios de los cambios efectuados. Pensado para mejorar robots
        y uso en juego distribuido
        '''
        pass
    def set_game(self,game):
        self._game = game
    def get_name(self):
        return self.Name

class Piece:
    '''
    Interfaz para las clases tipo pieza, como son el caballo y la reina
    '''
    _tablero = 0
    def __init__(self,owner):
        self._owner = owner
        self._log = logging(self._type)

    def set_tablero(self):
        if self._tablero == 0:
            self._tablero = tablero
        else:
            raise AjedrezError('Ficha ya colocada en tablero')

    def get_moves(self):
        '''
        Devuelve los movimientos validos
        '''
        return self._moves

    def get_type(self):
        return self._type

    def is_move_valid(self,positionS,positionF):
        '''
        Chequea que el movimiento sea valido.
        '''
        pass
    def __repr__(self):
        return self._type+str(self._owner)
    def __str__(self):
        return self._repr
    def get_owner(self):
        return self._owner

# ----------------------------------------------------------------------
class Juego:
    '''
    Clase encargada de interactuar con los jugadores, y de iniciar o terminar el juego
    '''
    _players = []
    _turn = -1
    def add_player(self,player):
        if player in self._players:
            raise JuegoError('Jugador ya en juego')
        elif self._status == 'STARTED':
            raise JuegoError('Juego ya iniciado')
        self._players.append(player)
        player.set_game(self)
    
    def start_game(self):
        if self._status == 'WAITING':
            self._status = 'STARTED'
        else: raise JuegoError('Juego en estado no correcto')
        self._change_turn()
        self._give_turn()

    def _change_turn(self):
        self.log.wrt('Cambiando turno')
        self._turn = (self._turn+1)%len(self._players)
        self.log.wrt(str(self._turn))
        for i in self._change_action:
            i()

    def _give_turn(self):
        while True:
            try:
                result = self._players[self._turn].get_turn()
                for i in self._action_turn:
                    i(result)
            except NextTurn:
                self._change_turn()
            except JuegoFinalizar:
                self._status = 'FINISH'
                #Modificar
                self._winner = self._turn
                print 'FIN'
                break
            except JuegoError:
                print 'ex'


            
        
    def _notify_event_all(self,msg):
        for i in self._players:
            i.notify_event[msg]

    def get_status(self):
        return self._status

    def get_turn(self):
        return self._players[self._turn]
    def get_winner(self):
        if self._status == 'FINISH':
            return self._winner

class DrawTablero:
    '''
    Clase encargada de dibujar el trablero
    '''
    pass
class Clock:
    '''
    Implementacion de un reloj, para restringir el tiempo a los jugadores
    '''
    pass

class Playback:
    '''
    TODO: Encargada del manejo del log de movimientos para su posterior visualizacion.
    '''
    pass


class Tablero(Juego):
    '''
    Clase encargada de la parte funcional del tablero
    '''

    _pieces={}
    _action_turn = []
    _action_finish = []
    _change_action = []
    _del_pieces = []
    _action_finish = []
    def __init__(self,x,y):
        self.log = logging('TABLERO')
        self._status = 'WAITING'
        self._misures = [x,y]
        self._change_action.append(self._change_clock)
        self._action_turn.append(self._move_from_to)
        self._change_action.append(self.draw)

    @classmethod
    def juego_clase(cls,x,y):
        inst = cls(x,y)
        inst._action_finish = inst._check_finish_clase
        return inst
    def _change_clock(self):
        print 'Reloj'

    def _check_finish_clase(self):
        try:
            if self.get_position(self.get_piece(type='REY')[0]).Y == 7:
                raise AjedrezError()
        except AjedrezError:
            self.draw()
            raise JuegoFinalizar(self._turn)
           
            
    def add_piece(self,piece,position):
        self.is_in_tablero(position)
        if not self.is_free(position):
                raise AjedrezError('Hueco ocupado por pieza')
        self._pieces[position] = piece
        

    def possible_moves_of(self,position):
        self.log.wrt('Devolviendo posibles movimientos')
        moves = self.get_piece(position = position).get_moves()
        positions = []
        for i in moves:
            try: 
                if len(position+i) == 1:
                    self._check_move_from_to(position,position+i)
                    positions.append(position+i)
                else: 
                    self.log.wrt(len(position+i))
                    for e in position+i:
                        self._check_move_from_to(position,e)
                        positions.append(e)
                        if can_eat(position,e):
                            raise AjedrezError('Ya no mais')
            except AjedrezError:
                self.log.wrt('ex')
                pass
        self.log.wrt(str(positions))
        return positions

    def _del_piece(self,position):
        self.log.wrt('Borrando pieza'+str(position))
        self._del_pieces.append(self._pieces[position])
        del self._pieces[position]
        
    def is_in_tablero(self,position):
        if not (self._misures[0] > position.X >= 0 and self._misures[1] > position.Y >= 0):
            raise AjedrezError('Position no situada dentro de tablero')
               
    def get_piece(self,position=0,type=0):
        try: 
            if position != 0:
                return self._pieces[position]
        except KeyError:
            raise AjedrezError('Position libre, no hay pieza en ella')
        if type != 0:
            a = []
            for i in self._pieces:
                if self._pieces[i].get_type() == type:
                    a.append(self._pieces[i])
            if len(a) != 0:
                return a
            raise AjedrezError('No hay fichas con ese tipo')
        
    def get_position(self,piece):
        for i in self._pieces:
            if self._pieces[i] == piece:
                return i
        raise AjedrezError('Esa pieza no existe en el tablero')

    def is_free(self,position):
        free = position in self._pieces
        #self.log.wrt(not free)
        return not free

    def can_eat(self,positionS,positionF):
        if not self.is_free(positionF):
            if self._pieces[positionS].get_owner() != self._pieces[positionF].get_owner():
                return True
            else:
                raise AjedrezError('Pieza con mismo dueño no puede ser comida')
        return False
            
    def _change_position(self,positionS,positionF):
        self.log.wrt('Cambiando de posicion a: '+str(positionS)+'->'+str(positionF))
        self._pieces[positionF] = self._pieces[positionS]
        del self._pieces[positionS]
    
    def _check_move_from_to(self,positionS,positionF):
        '''
        Cheque que el movimiento sea valido y sino lanza una excepcion.
        '''
        if self.is_free(positionS):
            raise AjedrezError('Hueco no ocupado')
        try :
            self.is_in_tablero(positionF)
            self._pieces[positionS].is_move_valid(positionS,positionF)
            self.can_eat(positionS,positionF)
        except AjedrezError:
            raise AjedrezError('Movimiento no posible ' +str('ex'))
    
    def _eat(self,positionS,positionF):
        if self.can_eat(positionS,positionF):
            self._del_piece(positionF)

    def _move_from_to(self,positions):
        '''
        Encargado de mover la pieza y su dueño
        '''
        positionS = positions[0]
        positionF = positions[1]
        try: 
            if not positionF in self.possible_moves_of(positionS):
                raise AjedrezError('No es un movimiento valido')
        except AjedrezError:
            raise JuegoError('ERROR ----------> '+str('ex'))
        
        self.log.wrt(self.get_turn())
        
        if self.get_turn() != self._pieces[positionS].get_owner():
            raise JuegoError('NO ES TU FICHA')
        self._eat(positionS,positionF)
        self._change_position(positionS,positionF)
        self._action_finish()
        raise NextTurn

    def draw(self):
        '''
        TODO: Crear Clase a parte
        '''
        print ' ',
        for x in range(self._misures[0]):
            print LETRAS[x],
        print 
        for y in range(self._misures[1]):
            print self._misures[0] - y,
            for x in range(self._misures[0]):
                if not self.is_free(Position(x,self._misures[0] - y -1)):
                    print str(self.get_piece(position=Position(x,self._misures[0] - y -1))),
                elif (x+y)%2 == 0:
                    print ' ',
                else:
                    print '#',
            print

    



'''
Implmentación de los tipos jugador y pieza
'''
class Caballo(Piece):
    _type = 'CABALLO'
    _moves = [Move(1,2),Move(2,1),Move(1,-2),Move(2,-1),Move(-1,2),Move(-1,-2),Move(-2,1),Move(-2,-1)]
    _repr = 'C'
class Rey(Piece):
    _type = 'REY'
    _moves = [Move(0,1),Move(0,-1),Move(1,0),Move(-1,0),Move(-1,1),Move(1,1),Move(1,-1),Move(-1,-1)]
    _repr = 'R'
class Reina(Piece):
    _type = 'REINA'
    _moves = [Vector(1,0),Vector(0,-1),Vector(1,0),Vector(-1,0),Vector(-1,1),Vector(1,1),Vector(1,-1),Vector(-1,-1)]
class Peon(Piece):
    _moves = [Move(0,1),Move(1,1),Move(1,-1),Move(0,-1),Move(-1,1),Move(-1,-1)]
    _type = 'PEON'
    def is_move_valid(self,positionS,positionF):
        move = positionF-positionS
        situation = self._tablero.get_piece(positionS).get_owner().get_situation()
        if situation == 7:
            a = -1
        elif situation == 0:
            a = 1
        else:
            raise AjedrezError('NO puede ser')
        for i in self._moves:
            if move == Move(0,a) and self._tablero.is_free(positionF):
                return 
            elif self._tablero.can_eat(positionF):
                return
        raise AjedrezError('YESss')

            
                
        
class Torre(Piece):
    pass
class Alfil(Piece):
    pass

class Robot(Player,object):
    def __init__(self,name):
        self.log = logging('R:'+str(name))
        self.Name = str(name)
    def __repr__(self):
        return 'Robot'


    def get_turn(self):
        print self.Name,'Tu turno'
        while True:
            jugadas = [self._comer_si_puede(),self._alejar_peligro()]
            for i in jugadas:
                if i:return i
            return self._mover_lejano()
    def _alejar_peligro(self):
        pieces = self._game.get_piece(type = 'CABALLO')
        rey = self._game.get_position(self._game.get_piece(type= 'REY')[0])
        piece = False
        for i in pieces:
            if len(self._game.get_position(i)-rey)<=sqrt(2):
                piece = i
                break
        if not piece:return False
        move = self._posicion_cercana(piece)
        return [self._game.get_position(piece),move]
    def _posicion_cercana(self,piece):
        rey = self._game.get_position(self._game.get_piece(type='REY')[0])
        moves = self._game.possible_moves_of(self._game.get_position(piece))
        dis = 5555555555555555555555555555
        for i in moves:
            if dis > len(i-rey)>sqrt(2):
                move,dis = i,len(i-rey)
        return move

    def _mover_lejano(self):
        pieces = self._game.get_piece(type='CABALLO')
        rey = self._game.get_position(self._game.get_piece(type='REY')[0])
        self.log.wrt('Moviendo el que este mas lejos')
        dis = 0
        for i in pieces:
            f = len(self._game.get_position(i)-rey)
            if f > dis:
                piece,dis = i,f
        move = self._posicion_cercana(piece)
        return [self._game.get_position(piece),move]
    def _comer_si_puede(self):
        pieces = self._game.get_piece(type='CABALLO')
        self.log.wrt(pieces)
        for i in pieces:
            position = self._game.get_position(i)
            moves = self._game.possible_moves_of(position)
            for a in moves:
                if self._game.can_eat(position,a):
                    return [position,a]
        return False
    def _aleatorio(self):
        pieces = self.caballos
        rand = random.randrange(len(pieces))
        position = self._game.get_position(pieces[rand])
        positions = self._game.possible_moves_of(position)
        rand2 = random.randrange(len(positions))
        self.log.wrt(str(rand2)+' '+str(positions))
        pF = positions[rand2]
        print position,'->',pF
        return [position,pF]
    def get_caballos(self):
        return self._game.get_piece(type='CABALLO')
    def noset(self,val):
        raise AjedrezError('No se puede asignar valores a caballos')
    caballos = property(get_caballos,noset)
class HumanoClase(Player):
    def __init__(self,name):
        self.Name = str(name)
        self.log = logging('H:'+self.Name)
        self.commands = ['w','x','d','a','q','e','c','z']
        self.CM = {}
        for i in range(len(self.commands)):
            self.CM[self.commands[i]] = Rey._moves[i]
    def get_turn(self):
        print 'Humano, turno'
        while True:
            a = raw_input('>>> ')
            try:
                move = self.CM[a]
                start = self._game.get_position(self._game.get_piece(type='REY')[0])
                self.log.wrt(str(move))
                self.log.wrt(str(start))
                return [start,start+move]
            except:
                print 'Usa uno de los siguientes'
                print self.commands

        


def main():
    table = Tablero.juego_clase(8,8)
    hum = HumanoClase('Enrique')
    hum2 = Robot('2')
    table.add_player(hum)
    table.add_player(hum2)
    table.add_piece(Rey(hum),Position(3,0))
    table.add_piece(Caballo(hum2),Position(0,7))
    table.add_piece(Caballo(hum2),Position(2,7))
    table.add_piece(Caballo(hum2),Position(4,7))
    table.add_piece(Caballo(hum2),Position(6,7))
    table.start_game()


if __name__ == '__main__':
    main()
