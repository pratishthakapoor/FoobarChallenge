import numpy as np

data = [[0,1,2,3,4,5,6,7], [8,9,10,11,12,13,14,15], [16,17,18,19,20,21,22,23],
        [24,25,26,27,28,29,30,31], [32,33,34,35,36,37,38,39], [40,41,42,43,44,45,46,47],
        [48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63]]

class ElementPosition:
    def __init__(self, index=None):
        if (index != None):
            self.col = int((index % 8) +  1)
            self.row = int((index / 8) + 1)

    @classmethod        
    def getElementLocation(cls, col, row):
        c = ElementPosition()
        c.col = col
        c.row = row 
        return c

def possibleMoves(srcLocation , destLocation):
    res = []
    ## All the position is calculated from the center element
    # North West 
    res.append(ElementPosition.getElementLocation(srcLocation.col-1, srcLocation.row-2))
    # West North
    res.append(ElementPosition.getElementLocation(srcLocation.col-2, srcLocation.row-1))
    # North East
    res.append(ElementPosition.getElementLocation(srcLocation.col+1, srcLocation.row-2))
    # East North
    res.append(ElementPosition.getElementLocation(srcLocation.col+2, srcLocation.row-1)) 
    # South East
    res.append(ElementPosition.getElementLocation(srcLocation.col+1, srcLocation.row+2))
    # East South
    res.append(ElementPosition.getElementLocation(srcLocation.col+2, srcLocation.row+1))
    # South west 
    res.append(ElementPosition.getElementLocation(srcLocation.col-1, srcLocation.row+2))
    # West South
    res.append(ElementPosition.getElementLocation(srcLocation.col-2, srcLocation.row+1))
    
    #print(res)

    for loc in res:
        if(loc.row < 1 or loc.row > 8 or loc.col < 1 or loc.col > 8):
            res.remove(loc)
        elif(loc.row == destLocation.row and loc.col == destLocation.col):
            return None
    return loc

def movementCount(srcLocation, destLocation):
    level = 1
    nextMove = []
    currentMove = possibleMoves(srcLocation, destLocation)
    #print(currentMove.col, currentMove.row)


    if currentMove == None:
        return level

    while True:
        level += 1

    for move in currentMove:
        next_level = possibleMoves(move, destLocation)
        if next_level == None:
                return level
        nextMove.extend(next_level)

    currentMove = nextMove
    nextMove = []


def answer(src, dest):
    
    srcLocation = ElementPosition(src)
    destLocation = ElementPosition(dest)

    #print(srcLocation.row, srcLocation.col) 
    #print(destLocation.row, destLocation.col)
    
    #level = 1
    #nextMove = []
    #currentMove = possibleMoves(srcLocation, destLocation)
    #print(currentMove.col, currentMove.row)

    #if the source and destination location is same then return 0
    if(srcLocation.row == destLocation.row and srcLocation.col == destLocation.col):
        return 0 

    return movementCount(srcLocation , destLocation)


       


print(answer(19,36))


