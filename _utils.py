def make_tuple(coords):
        temp = []
        for char in coords:
            temp.append(char)
        coords = tuple(temp)
        return coords

chess_to_array = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                  'e': 4, 'f': 5, 'g': 6, 'h': 7,  
                  '1': 7, '2': 6, '3': 5, '4': 4,
                  '5': 3, '6': 2, '7': 1, '8': 0   
                 }

array_to_chess = {
                  0: 8, 1: 7, 2: 6, 3: 5, 4: 4,
                  5: 3, 6: 2, 7: 1
                 }

alphabetize = {
               1: 'a', 2: 'b', 3: 'c', 4: 'd',
               5: 'e', 6: 'f', 7: 'g', 8: 'h'
               }