import string

files = 'abcdefgh'
ranks = '12345678'
squares = [f + r for r in ranks for f in files]

chessToArray = dict(zip(squares, range(64)))
arrayToChess = dict(zip(range(64), squares))

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

class Piece:
    symbol = '?' #override during subclass creation

    def __init__(self, color: bin, location: str):
        self.clr = color #0 == white, 1 == black
        self.loc = location
        self.has_moved = False

    def __repr__(self):
        return f'{type(self).__name__}({self.clr}, {self.loc!r})'

    @property
    def display_symbol(self):
        return self.symbol if self.clr == 0 else self.symbol.lower()

    def locate(self):
        return self.loc

    def friendly(self, other):
        return other is not None and other.clr == self.clr

    def getmoves(self, board):
        """Return a list of legal destination squares."""
        raise NotImplementedError

    def move(self, sq: str, board):
        target = board.get(sq)
        if target is not None and self.friendly(target):
            return "You cannot capture your own pieces"
        if sq in self.getmoves(board):
            del board[self.loc]
            board[sq] = self
            self.loc = sq
            self.has_moved = True
            visual_upd(board)
            printBoard()
        else:
            print("Has to be a legal square")

class King(Piece):
    symbol = 'K'
    def getmoves(self, board):
        pass

class Queen(Piece):
    symbol = 'Q'
    def getmoves(self, board):
        pass

class Bishop(Piece):
    symbol = 'B'
    def getmoves(self, board):
        legalmvs = []
        lusq = []
        ldsq = []
        rusq = []
        rdsq = []
        i = files.index(self.loc[0])
        j = ranks.index(self.loc[1])
        for offset in range(-1, -i - 1, -1):
            if -1 < j + offset < 8:
                ldsq.append(f'{files[i + offset]}{j + offset + 1}')
            if 0 < j - offset < 8:
                lusq.append(f'{files[i + offset]}{j - offset + 1}')
        for offset in range(1, 8 - i):
            if 0 < j - offset < 8:
                rdsq.append(f'{files[i + offset]}{j + offset + 1}')
            if j + offset < 9:
                rusq.append(f'{files[i + offset]}{j - offset + 1}')
        for sq in ldsq:
            if board.get(sq) is None:
                legalmvs.append(sq)
            else:
                if not self.friendly(board[sq]):
                    legalmvs.append(sq)
                else:
                     break
        for sq in lusq:
            if board.get(sq) is None:
                legalmvs.append(sq)
            else:
                if not self.friendly(board[sq]):
                    legalmvs.append(sq)
                else:
                        break
        for sq in rdsq:
            if board.get(sq) is None:
                legalmvs.append(sq)
            else:
                if not self.friendly(board[sq]):
                    legalmvs.append(sq)
                else:
                        break
        for sq in rusq:
            if board.get(sq) is None:
                legalmvs.append(sq)
            else:
                if not self.friendly(board[sq]):
                    legalmvs.append(sq)
                else:
                        break
        return legalmvs

class Knight(Piece):
    symbol = 'N'
    def getmoves(self, board):
        arraymoves = (-17, -15, -10, -6, 6, 10, 15, 17)
        legalmvs = []
        locindex = chessToArray[self.loc]
        for i in arraymoves:
            if locindex + i in range(64) and not self.friendly(board.get(arrayToChess[locindex + i])):
                legalmvs.append(arrayToChess[locindex + i])
        return legalmvs
            
class Rook(Piece):
    symbol = 'R'
    def getmoves(self, board):
            pass

class Pawn(Piece):
    symbol = 'P'
    def getmoves(self, board):
        return squares

CLASS_MAP = {'r': Rook, 'n': Knight, 'b': Bishop, 'q': Queen, 'k': King, 'p': Pawn}
BACK_RANK = ('r', 'n', 'b', 'q', 'k', 'b', 'n', 'r')

def make_pieces():
    pieces = []
    for clr, rank in [(0, 1), ('1', '8')]:
        for file, letter in zip(files, BACK_RANK):
            cls = CLASS_MAP[letter]
            pieces.append(cls(clr, str(file) + str(rank)))
        pawn_rank = '2' if clr == 0 else '7'
        for file in files:
            pieces.append(Pawn(clr, file + pawn_rank))
    return pieces

pieces = make_pieces()
board = {p.loc: p for p in pieces}


visual = ['-'] * 64

def visual_upd(board):
    for sq in squares:
        visual[chessToArray[sq]] = board[sq].display_symbol if sq in board else '-'

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


# --------- Testing ------------

print(board['c1'].getmoves(board))

board['b2'].move('b4', board)
print(board['c1'].getmoves(board))
board['c1'].move('b2', board)
print(board['b2'].getmoves(board))






