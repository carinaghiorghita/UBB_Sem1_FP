from domain import *
import random

class MoveAlgorithm: #improve later
    def nextMove(self,board):
        '''
        calculates the computer's next move based on the planes that were already hit
        :param board: the computer's opponent's board
        :return: a random valid move
        '''
        coords=[]
        hit=0
        for i in range(1,9):
            for j in range(1,9):
                if board.getdata(i,j)==-3:
                    if hit==0:
                        coords=[]
                        hit=1
                    if i-1>0 and board.getdata(i-1,j)!=1 and board.getdata(i-1,j)!=-3 and board.getdata(i-1,j)!=-4:
                        coords.append((i-1,j))
                    if i+1<9 and board.getdata(i+1,j) != 1 and board.getdata(i+1,j) != -3 and board.getdata(i+1,j)!=-4:
                        coords.append((i+1,j))
                    if j-1>0 and board.getdata(i,j-1)!=1 and board.getdata(i,j-1)!=-3 and board.getdata(i,j-1)!=-4:
                        coords.append((i,j-1))
                    if j+1<9 and board.getdata(i,j+1)!=1 and board.getdata(i,j+1)!=-3 and board.getdata(i,j+1)!=-4:
                        coords.append((i,j+1))
                elif hit==0 and board.getdata(i,j)!=1 and board.getdata(i,j)!=-3 and board.getdata(i,j)!=-4:
                    coords.append((i,j))
        if len(coords)!=0:
            return random.choice(coords)
        raise ValueError('Computer cannot make move')


class Game:
    def __init__(self,pboard,cboard,ai):
        self._pboard=pboard
        self._cboard = cboard
        self._ai=ai

    def playerMove(self,row,col):
        self._cboard.move(row,col)

    def compMove(self):
        coord=self._ai.nextMove(self._pboard)
        self._pboard.move(coord[0],coord[1])

    def placePlayerPlane(self):
        '''
        places the player's plane based on the input coordinates
        '''
        placed=1
        while placed:
            try:
                coord=input("Coord:")
                if not coord[0].isalpha() or not coord[1].isdigit():
                    raise PlaneError
                else:
                    row=coord[0].upper()
                    row = ord(row)-64
                    col = int(coord[1])
                    dir = input("Direction of plane:")
                    dir=dir.lower()
                self._pboard.placePlane(row, col, dir)
                placed = 0
            except PlaneError:
                print('Try other coordinates.')
                continue
            except DirectionError:
                print('Invalid direction.')
                continue
            except (ValueError,IndexError):
                print('Try other coordinates.')
                continue

    def placeCompPlane(self):
        '''
        picks random coordinates for the computer's plane and places it
        '''
        placed=1
        while placed:
            listDir=['up','down','left','right']
            dir=random.choice(listDir)
            row=random.randrange(9)
            col=random.randrange(9)
            if self._cboard.getdata(row,col)!=-1 or self._cboard.getdata(row,col)!=-2:
                try:
                    self._cboard.placePlane(row,col,dir)
                    placed=0
                except (ValueError,PlaneError):
                    continue
            else:
                continue

    def getPlayerBoard(self):
        return self._pboard

    def getCompBoard(self):
        return self._cboard

