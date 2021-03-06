from service import *
from tests import *

class UI:
    def __init__(self,game):
        self._game=game

    def _readPlayerMove(self):
        cmd=input('Coord:')
        if not cmd[0].isalpha() or not cmd[1].isdigit():
            raise PlaneError
        row=cmd[0].upper()
        return (ord(row)-64,int(cmd[1]))

    def start(self):
        bp=self._game.getPlayerBoard()
        bc=self._game.getCompBoard()
        print(bp)

        print('Welcome! Please place your planes.')
        print('Plane 1:')
        self._game.placePlayerPlane()
        print(bp)
        print('Plane 2:')
        self._game.placePlayerPlane()
        print(bp)

        self._game.placeCompPlane()
        self._game.placeCompPlane()
        print('Computer has placed planes randomly.')

        playerTurn=True
        while True:
            try:
                if playerTurn==True:
                    print('Your board:')
                    print(bp)
                    print("Computer's board:")
                    print(bc)
                    coord=self._readPlayerMove()
                    self._game.playerMove(coord[0],coord[1])
                else:
                    self._game.compMove()
                playerTurn=not playerTurn
            except PlaneError:
                print('Try other coordinates')
                continue
            except GameWonException:
                if playerTurn==True:
                    print(bc)
                    print('You won!')
                else:
                    print(bp)
                    print('You lost!')
                return
            except (ValueError,IndexError):
                continue

