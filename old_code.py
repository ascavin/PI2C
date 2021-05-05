
def utility(state,players):
	theWinner = isAdvantage(state)
	if players == theWinner :
		return 1
	if theWinner == None :
		return 0
	return -1

def MAX(state,player):
	if isWinning(state):
		return utility(state, player)
	res = float('-inf')
	for move in moves(state):
		break
	return False

class IsPossibleTo:

	
	def __init__(self,Grid,State):
		self.symbolAllies="W"
		self.symbolOpponent="B" 
		self.grid=Grid
		self.exitMove=exitMove()
		self.state=State.copy()

	def isContact(self):
		AlliesMarble=getMarbleLocation(self.state,self.symbolAllies)
		for elem in AlliesMarble:
			findNeighbor(self.state['board'],self.symbolOpponent)
		return False

	def aMarblesNextToAllies():
		return False

	def moveOpponentMarbleOutOfTheBoard():
		return False

	def moveOpponentMarbleOutOfTheBoard(self,danger=False):
		###################################################################### Find marble near border
		marbleNearToBorder=findMarbleNearBorder(self.grid,self.symbolOpponent)		
		neighborOfOpponentMarble={}
		neighborOfOpponentMarbleInside={}
		for marble in marbleNearToBorder:
			alliesMarbles= findNeighbor(self.grid,marble,self.symbolAllies)
			opponentMarbles =findNeighbor(self.grid,marble,self.symbolOpponent) #to check if align but not next to border
			neighborOfOpponentMarble[marble]=alliesMarbles
			neighborOfOpponentMarbleInside[marble]=opponentMarbles
		###################################################################### Compute ejecting marble
		#print(marbleNearToBorder)
		moves=[]			
		for key in neighborOfOpponentMarble :
			move=canEject1(self.grid,self.exitMove,key,neighborOfOpponentMarble[key])
			if(move):
				moves.append(move)
		 #print(moves)
		for key in neighborOfOpponentMarbleInside:
			move=canEject2(self.grid,self.exitMove,key,neighborOfOpponentMarbleInside[key],self.symbolAllies)
			if move:
				moves.append(move)
		#print(moves)
		###################################################################### Compute better move rate
		followingState=[]
		followingMoves=[]
		for move in moves:
			for elem in move:
				newState=self.state.copy()
				position=[]
				for i in reversed(elem[0:len(elem)-1]):
					position.append(i)
				newState=moveMarblesTrain(newState,position,elem[-1])	
				followingState.append(newState)
				followingMoves.append(elem)
		if danger :
			return followingMoves
		maxNeighbor=[]
		###################################################################### Select Move with rate
		for state in followingState:
			maxValue=countNeighbor(state,self.symbolAllies)
			maxNeighbor.append(maxValue)
		if maxNeighbor :
			result=maxNeighbor.index(max(maxNeighbor))
			return followingMoves[result]
		else : return None

	def isMyMarbleInDanger(self):
		locations=getMarbleLocation(self.state,self.symbolAllies)
		marbleInDanger=[]
		for location in locations :
			for border in getBorder():
				if (location == border):
					marbleInDanger.append(location)
		askDanger=IsPossibleTo(self.state['board'],self.state)
		askDanger.symbolAllies='B' 			#find if opponent can exit a marble is the same that if i can exit a marble of the opponent
		askDanger.symbolOpponent='W'
		result=askDanger.moveOpponentMarbleOutOfTheBoard(danger=True)
		return result
	
		
	def canIEscape(self):
		return False




def getMarbleLocation(state,symbol):
	locations=[] 
	for i,line in enumerate(state['board']):
		for e,column in enumerate(line) :
			if (state['board'][i][e]==symbol):
				locations.append((i,e))
	return locations

def countNeighbor(state,symbol):
	neighbors=[]
	locations=getMarbleLocation(state,symbol)
	for location in locations:
		neighbor=findNeighbor(state['board'],location,symbol)
		for e in neighbor:
			neighbors.append((e[0],e[1]))
	result=len(neighbors)
	return result

def canEject1(grid,exitMove,location,neighbor):
		exitDirection = exitMove[location]
		alliesGoodDirectionToEject=[]
		for marble in neighbor:
			for direction in exitDirection:
				if (marble[2]==opposite[direction]):
						alliesGoodDirectionToEject.append(marble)
		goodMoves=[]
		currentMove=[]
		for i,marble in enumerate(alliesGoodDirectionToEject) :
			if (checkAlign(grid,marble,marble[2])):
				currentMove.append((marble[0],marble[1]))
				currentMove.append(getAlign(grid,marble,marble[2]))
				if (checkAlign(grid,currentMove[-1],marble[2])):
					currentMove.append(getAlign(grid,currentMove[-1],marble[2]))
				currentMove.append(opposite[marble[2]])
				goodMoves.append(currentMove.copy())
				currentMove.clear()
		return goodMoves

def canEject2(grid,exitMove,location,neighbor,symbol):
	exitDirection = exitMove[location]
	marbleToMove={}
	move=[]
	for marble in neighbor:
		for direction in exitDirection:
			if (marble[2]==opposite[direction]):
				# print(grid)
				# print(marble)
				# print(marble[2])
				location=(marble[0]+directions[opposite[direction]][0],marble[1]+directions[opposite[direction]][1])
				i=1
				while (getMarble(grid,location[0]+(directions[opposite[direction]][0]*i),location[1]+(directions[opposite[direction]][1]*i))==symbol and i<=3):
						move.append((location[0]+directions[opposite[direction]][0]*i,location[1]+directions[opposite[direction]][1]*i))
						i=i+1
				if len(move)>2:
					marbleToMove[marble]=move.copy()
				move.clear()
	goodMoves=[]
	position=[]
	for elem in marbleToMove:
		for i in reversed(marbleToMove[elem]):
			position.append(i)
		position.append(elem[2])
		goodMoves.append(position)	
	return goodMoves





def exitMove():
	exitMove={
			(0,0):['NW','W','NE'],
			(0,1):['NW','NE'],
			(0,2):['NW','NE'],
			(0,3):['NW','NE'],
			(0,4):['NW','E','NE'],
			(1,5):['E','NE'],
			(2,6):['E','NE'],
			(3,7):['E','NE'],
			(4,8):['NE','E','SE'],
			(5,8):['E','SE'],
			(6,8):['E','SE'],
			(7,8):['E','SE'],
			(8,8):['SW','E','SE'],
			(8,7):['SE','SW'],
			(8,6):['SE','SW'],
			(8,5):['SE','SW'],
			(8,4):['SE','W','SW'],
			(7,3):['SE','W'],
			(6,2):['SE','W'],
			(5,1):['SE','W'],
			(4,0):['SW','W','NW'],
			(3,0):['W','NW'],
			(2,0):['W','NW'],
			(1,0):['W','NW']
		}
	return exitMove



def move(state, player):
	ask = IsPossibleTo(state)
	if (isContact()) :
		if (ask.moveOpponentMarbleOutOfTheBoard()):
			if (manyContact()):
				moves=computeMovesKeepingMaxNeighbour()
				validMoves=ValidMove(Moves)               # return valid possibilites
				outMove=chooseMove(validMove)
			else :
				move=computeMoveWithMaxMarble()
				outmove=ValidMoves(move)              
	else :
		if (ask.moveManyMarbles()):
			moves = computeMovesKeepingMaxNeighbour() # return many possibilites
			validMoves=ValidMove(Moves)               # return valid possibilites
			outMove=chooseMove(validMove)             # out move 
		else :
			if ( ask.aMarblesNextToAllies()):
				moves=computeSingleMarbleMove()       # return many possibilities
				validMoves=ValidMove(Moves)               # return valid possibilites
				outMove=chooseMove(validMove)             # out move
			else :
				outMove=[(None,None)]

def getBorder():
	border=[(0,0),
			(0,1),
			(0,2),
			(0,3),
			(0,4),
			(1,5),
			(2,6),
			(3,7),
			(4,8),
			(5,8),
			(6,8),
			(7,8),
			(8,8),
			(8,7),
			(8,6),
			(8,5),
			(8,4),
			(7,3),
			(6,2),
			(5,1),
			(4,0),
			(3,0),
			(2,0),
			(1,0)]
	return border

def findMarbleNearBorder(grid,opponentSymbol):
	opponentMarbles=findOpponentMarbles(grid,opponentSymbol)
	borders = getBorder()
	nextToBorder = []
	for marble in opponentMarbles :
		for border in borders:
			if (border==marble):
				nextToBorder.append(marble)
	return nextToBorder

def findOpponentMarbles(grid,opponentSymbol):
	borderMarbles = []
	for l,line in enumerate(grid):
		for c,column in enumerate(line):
			if (grid[l][c] == opponentSymbol):
				borderMarbles.append((l,c))
	return borderMarbles

def findNeighbor(grid,location,symbol):
	neighbors=[]
	if (location[1]<=7) :
		if (grid[location[0]][location[1]+1]==symbol):  #E
			neighbors.append((location[0],location[1]+1,'E'))
	if (location[1]>=1):
		if (grid[location[0]][location[1]-1]==symbol):  #W
			neighbors.append((location[0],location[1]-1,'W'))
	if (location[1]<=7 and location[0]<=7):
		if (grid[location[0]+1][location[1]+1]==symbol):  #SE
			neighbors.append((location[0]+1,location[1]+1,'SE'))
	if  (location[1]>=1 and location[0]>=1):
		if (grid[location[0]-1][location[1]-1]==symbol):  #NW
			neighbors.append((location[0]-1,location[1]-1,'NW'))
	if (location[0]>=1):
		if (grid[location[0]-1][location[1]]==symbol):  #NE
			neighbors.append((location[0]-1,location[1],'NE'))
	if (location[0]<=7) :
		if (grid[location[0]+1][location[1]]==symbol):  #SW
			neighbors.append((location[0]+1,location[1],'SW'))
	return neighbors

#try go contact with most neighbour of my color
#strategies:
#When contact with opponent
#Yes : -Is it possible de move opponenent marble out of the board ? 
#   -Yes : If different contact :
#            Yes : Compute wich valid move will keep the most neighbour and move out opponnent marble with maximum marbles to do it
#            No : Move out opponnent marble with maximum marbles to do it
#   -No : If different contact :
#           Yes : Will I lost a marble ?(Do I get a marbles next to the boarder and 2 opponent align with my marble)
#                   Yes : Can I escape ? ( Available position & no neighbour will out me)
#                           Yes : Try to go next to a neighbour select the marbles with the most marbles neighbours 'allies' or break the line
#                           No : Marble is lost go to No
#                   No : Do all my marbles are neighboor ?
#                           Yes : Can I move opponents marbles close to the border?
#                                    Yes : I do it with the maximum marble
#                                    No : Can I move a marble next to allie marble ?
#                                           Yes : do it 
#                                           No : Can I move a marble ? 
#                                                    yes : move marble
#                                                    no : pass 
#                            No : Can I move many marbles next to alies marble ? (all free to move)
#                                   yes : Do it with the maximum marble
#                                   no : Choose a marble the closest from border to move :
#                                           is it free to move ? :
#                                               yes : move it to the center
#                                                no : next marble if none pass                          
#           No :  Do all my marbles are neighboor ?
#                           Yes : Can I move opponents marbles close to the border?
#                                    Yes : I do it with the maximum marble
#                                    No : Can I move a marble next to allie marble ?
#                                           Yes : do it 
#                                           No : Can I move a marble ? 
#                                                    yes : move marble
#                                                    no : pass 
#                            No : Can I move many marbles next to alies marble ? (all free to move)
#                                   yes : Do it with the maximum marble
#                                   no : Choose a marble the closest from border to move :
#                                           is it free to move ? :
#                                               yes : move it to the center
#                                                no : next marble if none pass
#No :
#   Is it possible to move many marble (allies) ?
#        Yes : random of moves for move  with maximum number of marble keeping most neigbour 
#        No  : Can I move a marble next to allies marbles :
#                Yes : move  
#                No : Can I move a marble ?
#                        Yes : move 
#                        No : pass


	#for line in state['board']:
	#    for column in line:







Game = Abalone

if __name__=='__main__':
	def show(state):
		print('\n'.join([' '.join(line) for line in state['board']]))
		print()

	state, next = Abalone(['LUR', 'LRG'])

	state['board'][3][3] = 'B'
	state['board'][4][3] = 'W'

	#state['board'][3][3] = 'B'
	#state['board'][2][0] = '0' #line, column
	#findMarbleNearBorder(state['board'])
	#state = moveMarblesTrain(state, [(1, 3), (2, 3), (3, 3)], 'SW')
	show(state)
	ask=IsPossibleTo(state['board'],state)
	#result=ask.moveOpponentMarbleOutOfTheBoard()
	result=ask.isMyMarbleInDanger()
	print(result)

	#show(state)
	#state = moveMarblesTrain(state, [(2,2)], 'SW')
	#show(state)
	#state = moveMarblesTrain(state, [(1, 3), (2, 3), (3, 3)], 'SW')
	#show(state)
	#state = moveMarblesTrain(state, [(2, 3), (3, 3), (4, 3)], 'SW')
	#show(state)
	#state = moveMarblesTrain(state, [(3, 3), (4, 3), (5, 3)], 'SW')
	#show(state)
