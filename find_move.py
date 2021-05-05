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
directions = {
	    'NE': (-1,  0),
	    'SW': ( 1,  0),
	    'NW': (-1, -1),
	    'SE': ( 1,  1),
	    'E': ( 0,  1),
	    'W': ( 0, -1)
    }
def findMove(grid,marble,symbol):
    moves=[]
    alignement=[]
    possibilities=[]
    for direction in directions :
        #print('test diretion :',direction)
        find=True
        e=1
        while find and e<5:           
            #print("neighbor",(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e))
            alignement.append(neighbor(grid,(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e)))
            possibilities=getPossibilities(symbol)
            for i,possibilitie in enumerate(possibilities):
                #print("-------------------------")      
                if possibilitie == alignement :
                    #print("possibilitie",possibilitie)
                    #print("alignement",alignement)
                    alignement.clear()
                    find=False
                    if i == 0: 
                        moves.append([[[marble[0],marble[1]]],direction])
                    if i == 1: 
                        moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]]],direction])
                    if i == 2:
                        moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]],[marble[0]+directions[direction][0]*2,marble[1]+directions[direction][1]*2]],direction])
                    if i == 3:
                        moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]]],direction])
                    if i == 4:
                        pass
                    if i == 5:
                        pass
                    if i == 6:
                        moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]],[marble[0]+directions[direction][0]*2,marble[1]+directions[direction][1]*2]],direction])
                    if i == 7:
                        moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]],[marble[0]+directions[direction][0]*2,marble[1]+directions[direction][1]*2]],direction])
                    break
            e=e+1   
    return moves


            
def neighbor(grid,marble):
    if move.isOnBoard(marble) :
        return grid[marble[0]][marble[1]]
    else : return 'E'

def getPossibilities(symbol):
        if symbol == 'W':         
            possibilities =[
                            ['E'],                 #:True,    #0
                            ['W','E'],             #:True,    #1
                            ['W','W','E'],         #:True,    #2
                            ['W','B','E'],         #:True,    #3
                            ['W','B','B'],         #:False,   #4
                            ['W','W','W'],         #:False,   #5
                            ['W','W','B','E'],     #:True,    #6
                            ['W','W','B','B','E'], #:True,    #7
                            ['W','W','B','B','B'], #:False,   #8
                            ]
            return possibilities
        else :
            possibilities =[
                            ['E'],                 #:True,    #0
                            ['B','E'],             #:True,    #1
                            ['B','B','E'],         #:True,    #2
                            ['B','W','E'],         #:True,    #3
                            ['B','W','W'],         #:False,   #4
                            ['B','B','B'],         #:False,   #5
                            ['B','B','W','E'],     #:True,    #6
                            ['B','B','W','W','E'], #:True,    #7
                            ['B','B','W','W','W'], #:False,   #8
                            ]
            return possibilities

if __name__=='__main__':  
    grid=[
			['W', 'W', 'W', 'W', 'W', 'W', 'X', 'X', 'X'],
			['W', 'W', 'W', 'W', 'W', 'W', 'X', 'X', 'X'],
			['E', 'E', 'W', 'W', 'W', 'E', 'E', 'X', 'X'],
			['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'X'],
			['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
			['X', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
			['X', 'X', 'E', 'E', 'B', 'B', 'B', 'E', 'E'],
			['X', 'X', 'X', 'B', 'B', 'B', 'B', 'B', 'B'],
			['X', 'X', 'X', 'X', 'B', 'B', 'B', 'B', 'B']
        ]
    result=findMove(grid,(8,8),'B')
    print(result)

            
    

