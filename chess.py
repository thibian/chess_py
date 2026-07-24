class Utils:
    @staticmethod
    def make_tuple(coords):
        Utils.empty = []
        for char in coords:
            Utils.empty.append(char)
        Utils.coords = tuple(Utils.empty)
        return Utils.coords


class Chess():
    def __init__(self):
        self.captured_pieces = []

    boardstate = [['R', 'N', 'B', 'Q', 'K', 'B', 'N','R'],
                  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                  ['_', '_', '_', '_', '_', '_', '_', '_'],
                  ['_', '_', '_', '_', '_', '_', '_', '_'],
                  ['_', '_', '_', '_', '_', '_', '_', '_'],
                  ['_', '_', '_', '_', '_', '_', '_', '_'],
                  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                  ['R', 'N', 'B', 'Q', 'K', 'B', 'N','R']]
        
    coords = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
              'e': 4, 'f': 5, 'g': 6, 'h': 7,  
              '1': 7, '2': 6, '3': 5, '4': 4,
              '5': 3, '6': 2, '7': 1, '8': 0
              }

    def checksquare(self, col, row):
        col = self.coords[col.lower()]
        row = self.coords['{0}'.format(row)]
        if self.checksquare(col, row) == '_':
            return False
        if self.checksquare(col, row) != '_':
            return True
        else:
            print("Please check the coordinate input")

    def move_piece(self, piece, col, row):
        if self.checksquare(col, row) == '_':
            col = self.coords[col.lower()]
            row = self.coords['{0}'.format(row)]
            self.boardstate[row][col] = piece
        if self.checksquare(col, row) != '_':
            print("Please move to an empty square")

class Piece(Chess):
    def __init__(self, symbol='A', color=0, currentsquare='A1'):
        self.color = color
        self.currentsquare = Utils.make_tuple(currentsquare)

    def locate(self):
        return self.coord

    def move(self, destination):
        self.destination = Utils.make_tuple(destination)
        self.dcol = self.destination[0]
        self.drow = self.destination[1]
        self.dcol = Chess.coords[self.dcol.lower()]
        self.drow = Chess.coords['{0}'.format(self.drow)]
        Chess.boardstate[self.drow][self.dcol] = self.symbol
        self.ccol = Chess.coords[self.currentsquare[0].lower()]
        self.crow = Chess.coords[self.currentsquare[1]]
        Chess.boardstate[self.crow][self.ccol] = '_'

        
class Knight(Piece):
    def __init__(self, symbol='N', color=0, currentsquare='B1'):
        self.symbol = symbol
        self.color = color
        self.currentsquare = Utils.make_tuple(currentsquare)

import turtle






