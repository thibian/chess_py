import string

def make_tuple(coords):
        temp = []
        for char in coords:
            temp.append(char)
        coords = tuple(temp)
        return coords

keys = []
for x in range(1, 9):
      for y in string.ascii_lowercase[0: 8]:
            fusion = y + str(x)
            keys.append(fusion)

nums = list(range(64))

chessToArray = dict(zip(keys, nums))
arrayToChess = dict(zip(nums, keys))

