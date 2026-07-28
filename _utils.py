import string

def make_tuple(coords):
        temp = []
        for char in coords:
            temp.append(char)
        coords = tuple(temp)
        return coords

files = 'abcdefgh'
ranks = '12345678'
squares = [f + r for r in ranks for f in files]

chessToArray = dict(zip(squares, range(64)))
arrayToChess = dict(zip(range(64), squares))

