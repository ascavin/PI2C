import move

def findNeighbor(grid,location,symbol,varstate=False):
	neighbors=[]
	isneigbour = False
	dictneighbour = {}
	if (location[1]<=7) :
		if (grid[location[0]][location[1]+1]==symbol):  #E
			neighbors.append((location[0],location[1]+1,'E'))
			dictneighbour["E"] = (location[0],location[1]+1)
			isneigbour = True
	if (location[1]>=1):
		if (grid[location[0]][location[1]-1]==symbol):  #W
			neighbors.append((location[0],location[1]-1,'W'))
			dictneighbour["W"] = (location[0],location[1]-1)
			isneigbour = True
	if (location[1]<=7 and location[0]<=7):
		if (grid[location[0]+1][location[1]+1]==symbol):  #SE
			neighbors.append((location[0]+1,location[1]+1,'SE'))
			dictneighbour["SE"] = (location[0]+1,location[1]+1)
			isneigbour = True
	if  (location[1]>=1 and location[0]>=1):
		if (grid[location[0]-1][location[1]-1]==symbol):  #NW
			neighbors.append((location[0]-1,location[1]-1,'NW'))
			dictneighbour["NW"] = (location[0]-1,location[1]-1)
			isneigbour = True
	if (location[0]>=1):
		if (grid[location[0]-1][location[1]]==symbol):  #NE
			neighbors.append((location[0]-1,location[1],'NE'))
			dictneighbour["NE"] = (location[0]-1,location[1])
			isneigbour = True
	if (location[0]<=7) :
		if (grid[location[0]+1][location[1]]==symbol):  #SW
			neighbors.append((location[0]+1,location[1],'SW'))
			dictneighbour["SW"] = (location[0]+1,location[1])
			isneigbour = True

	if varstate == True :
		return isneigbour,dictneighbour
	return neighbors

def findMove(grid,marble,symbol,opponentSymbol):
    directions = {
	    'NE': (-1,  0),
	    'SW': ( 1,  0),
	    'NW': (-1, -1),
	    'SE': ( 1,  1),
	    'E': ( 0,  1),
	    'W': ( 0, -1)
    }
    neighborPosition={}
    alignement=[]
    for direction in directions :
        i=1
        while condition(alignement):
            


def validNeighborPosition(position,direction):
    if move.isnotOnBoard(position):
        return False
    else : return True

def condition(alignement,symbol):
    validMove =[
                    ['E'],
                    ['W','E'],
                    ['W','B','E'],
                    ['W','B','B'],
                    ['W','W','W'],
                    ['W','W','B','E'],
                    ['W','W','B','B','E'],
                    ['W','W','B','B','B'],
                    ]
    
    e=0
    for i,possibilitie in possibilities:
        if possibilitie == alignement :
            return True
    return False

            
    


            
    

