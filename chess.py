from _utils import chess_to_array, array_to_chess, alphabetize

boardstate = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
              ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
              ['_', '_', '_', '_', '_', '_', '_', '_'],
              ['_', '_', '_', '_', '_', '_', '_', '_'],
              ['_', '_', '_', '_', '_', '_', '_', '_'],
              ['_', '_', '_', '_', '_', '_', '_', '_'],
              ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
              ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        

def checksquare(col: str, row: str):
    col = chess_to_array[col.lower()]
    row = chess_to_array[row]
    if boardstate[row][col] == '_':
        return False
    if boardstate[row][col] != '_':
        return True

class Piece:
    def __init__(self, color: bin, location: tuple):
        self.color = color
        self.location = location

    def locate(self):
        return self.location

    def update_location(self, col, row):
        self.location = (col, row)

    def friendly(self, other):
        if other.color == self.color:
            return True
        else:
            return False

    def move(self, destination: tuple):
        if not checksquare(*destination):
            self.update_location(*destination)
        if checksquare(*destination):
            try: 
                self.capture()
            except: 
                print("The square you are trying to move to either doesn't exist " \
                "or is occupied by a friendly piece.") 

    def capture(self, destination):
        if not self.friendly:
            self.update_location(*destination)

class Knight(Piece):
    symbol = 'K'
    
knight = Knight(0, ('g', '1'))

knight.move(('f', '3'))
print(knight.locate())

knight.move(('e', '2'))

