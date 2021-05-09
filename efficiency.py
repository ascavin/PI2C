import move as find 
import find_move 
import copy
symbols = ['B', 'W']

directions = {
	'NE': (-1,  0),
	'SW': ( 1,  0),
	'NW': (-1, -1),
	'SE': ( 1,  1),
	 'E': ( 0,  1),
	 'W': ( 0, -1)
}

def getMarbleLocation(state,symbol):
	locations=[] 
	for i,line in enumerate(state['board']):
		for e,column in enumerate(line) :
			if (state['board'][i][e]==symbol):
				locations.append((i,e))
	return locations


def marbleCount(state,symbol):
	result=getMarbleLocation(state,symbol)
	return len(result)

def neighbor(grid,marble):
	#print(marble)
	if  marble[0]>=0 and marble[0]<=8 and marble[1]<=8 and marble[1]>=0:
		res=grid[marble[0]][marble[1]]
		if res=='X':
			res='E'
		return res
	else : return 'E'

def countNeighbor(state,symbol):
	marbles=getMarbleLocation(state,symbol)
	neighbors=0
	for marble in marbles:
		for direction in directions:
			position=(marble[0]+directions[direction][0],marble[0]+directions[direction][1])
			if find_move.neighbor(state['board'],position)==symbol:
				if neighbor(state['board'],position)==symbol:
					neighbors=neighbors+1
	return neighbors

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

def 

def findMarbleNearBorder(state,symbol):
	marbles=getMarbleLocation(state,symbol)
	borders = getBorder()
	nextToBorder = []
	for marble in marbles :
		for border in borders:
			if (border==marble):
				nextToBorder.append(marble)
	return nextToBorder


def advantage(state,symbol):
	me = marbleCount(state,symbol)
	you = marbleCount(state,find.opponent(symbol))
	if me > you :
		return symbols[state['current']]
	elif you > me :
		return find.opponent(symbols[state['current']])
	else : 
		return None

def valueOfState(state):
	advantage = marbleCount(state,find.opponent(symbols[state['current']]))
	border = len(findMarbleNearBorder(state,find.opponent(symbols[state['current']])))
	result = 1000-100*advantage+10*border
	print(result)
	return 1000-100*advantage+10*border

def valueOfMove(state,move,symbol):
	def show(state):
		print('\n'.join([' '.join(line) for line in state['board']]))
		print()
	previousNeighborAllies = countNeighbor(state,symbols[state['current']])
	previousNeighborOpponent = countNeighbor(state,find.opponent(symbols[state['current']]))
	previousAdvantage = marbleCount(state,find.opponent(symbols[state['current']]))
	previousNearBorder = len(findMarbleNearBorder(state,find.opponent(symbols[state['current']])))
	#show(state)
	newState=find.moveMarblesTrain(state,move[0],move[1])
	#show(newState)
	nextNeighborAllies = countNeighbor(newState,symbols[state['current']])
	nextNeighborOpponent = countNeighbor(state,find.opponent(symbols[state['current']]))
	nextAdvantage = marbleCount(newState,find.opponent(symbols[state['current']]))
	nextNearBorder = len(findMarbleNearBorder(newState,find.opponent(symbols[state['current']])))
	value = 0
	if previousAdvantage > nextAdvantage :
		value = value+100
	elif previousAdvantage < nextAdvantage:
		value = value-100	
	if previousNearBorder<nextNearBorder :
		value = value+50
	elif previousNearBorder > nextNearBorder :
		value = value-50
	diffAllies = nextNeighborAllies- previousNeighborAllies
	diffOpponent = nextNeighborOpponent - previousNeighborOpponent
	value = value + diffAllies + (diffOpponent+1)*2
	return value

if __name__=='__main__':
	state={'players': ['toto2', 'toto1'],
			'current': 0,
	  		'board': [['W', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X'],
	  			['W', 'W', 'W', 'W', 'W', 'W', 'X', 'X', 'X'],
	    		['E', 'E', 'W', 'W', 'W', 'E', 'E', 'X', 'X'],
		 		['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'X'],
		 		['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
		   		['X', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E'],
		    	['X', 'X', 'E', 'B', 'E', 'B', 'B', 'E', 'E'],
			 	['X', 'X', 'X', 'B', 'E', 'B', 'B', 'B', 'B'],
			  	['X', 'X', 'X', 'X', 'B', 'B', 'B', 'B', 'B']]
		}
	moves=[[[[8, 8], [7, 8]], 'NE'], [[[8, 8]], 'SW'], [[[8, 8], [7, 7], [6, 6]], 'NW'], [[[8, 8]], 'SE'], [[[8, 8]], 'E']]
	values=[]
	for i,move in enumerate(moves):
		values.append(valueOfMove(state,move,symbols[state['current']]))
	choice=max(values)
	move=values.index(choice)
	print(moves[move])


		