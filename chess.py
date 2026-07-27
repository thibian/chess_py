import _utils
from _utils import chessToArray, arrayToChess

board = ['r01', 'n01', 'b01', 'q0', 'k0', 'b02', 'n02', 'r02', 
         'p01', 'p02', 'p03', 'p04', 'p05', 'p06', 'p07', 'p08', 
         'v', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 
         'v', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 
         'v', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 
         'v', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 
         'p18', 'p17', 'p16', 'p15', 'p14', 'p13', 'p12', 'p11', 
         'r12', 'n12', 'b12', 'q1', 'k1', 'b11', 'n11', 'r11']

visual = [
    'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R',
    'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
    '-', '-', '-', '-', '-', '-', '-', '-',
    '-', '-', '-', '-', '-', '-', '-', '-',
    '-', '-', '-', '-', '-', '-', '-', '-',
    '-', '-', '-', '-', '-', '-', '-', '-',
    'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
    'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R',
]


def squareempty(sq="a1"):
    if board[chessToArray[sq]] == 'v':
        return True
    if board[chessToArray[sq]] != 'v':
        return False


class Piece:
    def __init__(self, color: bin, location: str, name: str):
        self.clr = color
        self. name = name
        self.loc = location
        self._loc = chessToArray[location]

    def locate(self):
        return self.loc

    def loc_upd(self, square):
        self.loc = square
        self._loc = (chessToArray[square])
        visual_upd()
        printBoard()

    def friendly(self, other):
        other = eval(other)
        if other.clr == self.clr:
            return True
        else:
            return False

    def move(self, sq: str):
        if squareempty(sq):
            board[self._loc], board[chessToArray[sq]] = 'v', self.name
            self.loc_upd(sq)
        elif not squareempty(sq):
            self.capture(sq)

    def capture(self, sq):
        if not self.friendly(board[chessToArray[sq]]):
            board[self._loc], board[chessToArray[sq]] = 'v', self.name
            self.loc_upd(sq)
        elif self.friendly(board[chessToArray[sq]]):
            return "You cannot capture your own pieces"
        else:
            return "Please enter a valid target square"

    def iscaptured(self):
        if board[self._loc] == str(self):
            return False
        else:
            return True

class King(Piece):
    symbol = 'K'

class Queen(Piece):
    symbol = 'Q'

class Bishop(Piece):
    symbol = 'B'

class Knight(Piece):
    symbol = 'N'

class Rook(Piece):
    symbol = 'R'

class Pawn(Piece):
    symbol = 'P'

k0 = King(0, 'e1', 'k0')
k1 = King(1, 'e8', 'k1')

q0 = Queen(0, 'd1', 'q0')
q1 = Queen(1, 'd8', 'q1')

r01 = Rook(0, 'a1', 'r01')
r02 = Rook(0, 'h1', 'r02')
r11 = Rook(1, 'h8', 'r11')
r12 = Rook(1, 'a8', 'r12')

n01 = Knight(0, 'b1', 'n01')
n02 = Knight(0, 'g1', 'n02')
n11 = Knight(1, 'g8', 'n11')
n12 = Knight(1, 'b8', 'n12')

b01 = Bishop(0, 'c1', 'b01')
b02 = Bishop(0, 'f1', 'b02')
b11 = Bishop(1, 'f8', 'b11')
b12 = Bishop(1, 'c8', 'b12')

p01 = Pawn(0, 'a2', '')
p02 = Pawn(0, 'b2', '')
p03 = Pawn(0, 'c2', '')
p04 = Pawn(0, 'd2', '')
p05 = Pawn(0, 'e2', '')
p06 = Pawn(0, 'f2', '')
p07 = Pawn(0, 'g2', '')
p08 = Pawn(0, 'h2', '')

p18 = Pawn(1, 'a7', '')
p17 = Pawn(1, 'b7', '')
p16 = Pawn(1, 'c7', '')
p15 = Pawn(1, 'd7', '')
p14 = Pawn(1, 'e7', '')
p13 = Pawn(1, 'f7', '')
p12 = Pawn(1, 'g7', '')
p11 = Pawn(1, 'h7', '')

piecenames = [
      'r01', 'n01', 'b01', 'q0', 'k0', 'b02', 'n02', 'r02', 
      'p01', 'p02', 'p03', 'p04', 'p05', 'p06', 'p07', 'p08', 
      'p18', 'p17', 'p16', 'p15', 'p14', 'p13', 'p12', 'p11', 
      'r12', 'n12', 'b12', 'q1', 'k1', 'b11', 'n11', 'r11',
      ]

pieces = [
    r01, n01, b01, q0, k0, b02, n02, r02, 
    p01, p02, p03, p04, p05, p06, p07, p08, 
    p18, p17, p16, p15, p14, p13, p12, p11, 
    r12, n12, b12, q1, k1, b11, n11, r11,
]

convert = dict(zip(piecenames, pieces))
for name, piece in zip(piecenames, pieces):
    piece.name = name

def visual_upd():
    for i, key in enumerate(board):
        if key == 'v':
            visual[i] = '-'
            continue
        name = convert[key]
        visual[i] = name.symbol

def printBoard():
    x = 56    
    while True:
        for i in range(x, x+8):
            print(visual[i], end=" ")
        print("")
        x -= 8
        if x == -8:
            print("")
            break

printBoard()
p05.move('e4')
p15.move('d5')
p05.move('d5')





