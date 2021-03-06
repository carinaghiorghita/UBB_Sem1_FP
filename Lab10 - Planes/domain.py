from exceptions import *
from texttable import Texttable

class Board:
    def __init__(self,player):
        # 0 - empty cell
        # 1 - empty cell that has been already targeted
        #-1 - cell has plane
        #-2 - cell has cockpit
        #-3 - cell has plane and has been hit
        #-4 - cell is part of a plane that has been taken down
        self._player=player
        self._planes=[]
        self._data=[]
        for i in range(9):
            self._data.append([0]*9)

    def getdata(self,x,y):
        return self._data[x][y]

    def placePlane(self,row,col,dir):
        '''
        checks whether the plane can be placed at the coordinates given and then places the plane
        :param row: row of cockpit
        :param col: column of cockpit
        :param dir: direction of the plane
        '''
        placed=1
        if dir=='up':
            if row not in range (2,7) or col not in range (3,7):
                raise PlaneError()
            for i in range(row-1,row+3):
                if self._data[i][col]==-1:
                    placed=0
            for i in range(col-2,col+3):
                if self._data[row][i]==-1:
                    placed=0
            for i in range(col-1,col+2):
                if self._data[row+2][i]==-1:
                    placed=0
            if placed==1:
                for i in range(row-1,row+3):
                    self._data[i][col]=-1
                for i in range(col-2,col+3):
                    self._data[row][i]=-1
                for i in range(col-1,col+2):
                    self._data[row+2][i]=-1
                self._data[row][col]=-2
                self._planes.append(Plane(row,col,dir))
            else:
                raise PlaneError()
        elif dir=='down':
            if row not in range (3,8) or col not in range (3,7):
                raise PlaneError()
            for i in range(row-2,row+2):
                if self._data[i][col]==-1:
                    placed=0
            for i in range(col-2,col+3):
                if self._data[row][i]==-1:
                    placed=0
            for i in range(col-1,col+2):
                if self._data[row-2][i]==-1:
                    placed=0
            if placed==1:
                for i in range(row-2,row+2):
                    self._data[i][col]=-1
                for i in range(col-2,col+3):
                    self._data[row][i]=-1
                for i in range(col-1,col+2):
                    self._data[row-2][i]=-1
                self._data[row][col]=-2
                self._planes.append(Plane(row, col, dir))
            else:
                raise PlaneError()
        elif dir=='left':
            if row not in range(3,7) or col not in range(2,7):
                raise PlaneError()
            for i in range(col-1,col+3):
                if self._data[row][i]==-1:
                    placed=0
            for i in range(row-2,row+3):
                if self._data[i][col]==-1:
                    placed=0
            for i in range(row-1,row+2):
                if self._data[i][col+2]==-1:
                    placed=0
            if placed==1:
                for i in range(col-1,col+3):
                    self._data[row][i]=-1
                for i in range(row-2,row+3):
                    self._data[i][col]=-1
                for i in range(row-1,row+2):
                    self._data[i][col+2]=-1
                self._data[row][col]=-2
                self._planes.append(Plane(row, col, dir))
            else:
                raise PlaneError()
        elif dir=='right':
            if row not in range(3,7) or col not in range(3,8):
                raise PlaneError()
            for i in range(col-2,col+2):
                if self._data[row][i]==-1:
                    placed=0
            for i in range(row-2,row+3):
                if self._data[i][col]==-1:
                    placed=0
            for i in range(row-1,row+2):
                if self._data[i][col-2]==-1:
                    placed=0
            if placed==1:
                for i in range(col-2,col+2):
                    self._data[row][i]=-1
                for i in range(row-2,row+3):
                    self._data[i][col]=-1
                for i in range(row-1,row+2):
                    self._data[i][col-2]=-1
                self._data[row][col]=-2
                self._planes.append(Plane(row, col, dir))
            else:
                raise PlaneError()
        else:
            raise DirectionError()

    def isWon(self):
        '''
        checks whether the game is won (there are no more planes that haven't been hit)
        :return: True if won, False if the game can continue
        '''
        for p in self._planes:
            if p.hit == 0:
                return False
        return True

    def move(self,row,col):
        '''
        checks whether the move is valid, if yes it makes the move and then checks if the game is won
        :param row: row of move
        :param col: column of move
        '''
        if row not in range(1,9) or col not in range(1,9):
            raise ValueError('Move outside board')
        if self._data[row][col]==1 or self._data[row][col]==-3:
            raise ValueError('Cell has already been hit')
        elif self._data[row][col]==0:
            self._data[row][col]=1
        elif self._data[row][col]==-1:
            self._data[row][col]=-3
        elif self._data[row][col]==-2:
            for p in self._planes:
                if p.getRow()==row and p.getCol()==col:
                    dir=p.getDir()
                    if dir=='up':
                        for i in range(row - 1, row + 3):
                            self._data[i][col] = -4
                        for i in range(col - 2, col + 3):
                            self._data[row][i] = -4
                        for i in range(col - 1, col + 2):
                            self._data[row + 2][i] = -4
                    elif dir=='down':
                        for i in range(row - 2, row + 2):
                            self._data[i][col] = -4
                        for i in range(col - 2, col + 3):
                            self._data[row][i] = -4
                        for i in range(col - 1, col + 2):
                            self._data[row - 2][i] = -4
                    elif dir=='left':
                        for i in range(col - 1, col + 3):
                            self._data[row][i] = -4
                        for i in range(row - 2, row + 3):
                            self._data[i][col] = -4
                        for i in range(row - 1, row + 2):
                            self._data[i][col+2] = -4
                    else:
                        for i in range(col - 2, col + 2):
                            self._data[row][i] = -4
                        for i in range(row - 2, row + 3):
                            self._data[i][col] = -4
                        for i in range(row - 1, row + 2):
                            self._data[i][col-2] = -4
                    p.hit=1
        if self.isWon():
            raise GameWonException()

    def __str__(self):
        t=Texttable()
        if self._player=='player':
            d={0:' ',1:'O',-1:'P',-2:'C',-3:'X',-4:'D'}
        else:
            d={0:' ',1:'O',-1:' ',-2:' ',-3:'X',-4:'D'}
        row = [' ']
        for i in range(1, 9):
            row.append(i)
        t.add_row(row)
        for i in range(1, 9):
            row = self._data[i][:]  # copy of the initial list
            row[0] = chr(64 + i)
            for j in range(1, 9):
                row[j] = d[row[j]]
            t.add_row(row)
        return (t.draw())

class Plane:
    def __init__(self,row,col,dir):
        self._row = row
        self._column = col
        self._direction = dir
        self.hit=0

    def getRow(self):
        return self._row

    def getCol(self):
        return self._column

    def getDir(self):
        return self._direction
    def __str__(self):
        return "Plane on row "+str(self._row)+" and col "+str(self._column)+" and dir "+str(self._direction)
