import move as mv 
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

def getMarbleLocation(state,symbol):#return the location of a marble 
	locations=[] 
	for i,line in enumerate(state['board']):
		for e,column in enumerate(line) :
			if (state['board'][i][e]==symbol):
				locations.append((i,e))
	return locations


def marbleCount(state,symbol):# count the total number of white marbles or black marbles on the board 
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
			if mv.insidetheboard(state['board'],position)==symbol:
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

def getCrownSecond():
	crown = [
		(1,1),
		(2,1),
		(3,1),
		(4,1),
		(5,2),
		(6,3),
		(7,4),
		(7,5),
		(7,6),
		(7,7),
		(6,7),
		(5,7),
		(4,7),
		(3,6),
		(2,5),
		(1,4),
		(1,3),		
		(1,2)
		]
	return crown
def getCrownCenter():
	crown = [
		(2,2),
		(2,3),
		(2,4),
		(3,2),
		(3,3),
		(3,4),
		(3,5),
		(4,2),
		(4,3),
		(4,4),
		(4,5),
		(4,6),
		(5,3),
		(5,4),
		(5,5),
		(5,6),
		(6,4),		
		(6,5),
		(6,6)
		]
	return crown



def findMarbleNearBorder(state,symbol):
	marbles=getMarbleLocation(state,symbol)
	borders = getBorder()
	nextToBorder = []
	for marble in marbles :
		for border in borders:
			if (border==marble):
				nextToBorder.append(marble)
	return nextToBorder

def findMarbleCrownCenter(state,symbol):
	marbles=getMarbleLocation(state,symbol)
	crownCenters = getCrownCenter()
	marbleInCenter= []
	for marble in marbles :
		for crownCenter in crownCenters:
			if (crownCenter==marble):
				marbleInCenter.append(marble)
	return marbleInCenter

def findMarbleCrownSecond(state,symbol):
	marbles=getMarbleLocation(state,symbol)
	crownSeconds = getCrownSecond()
	marbleInSecond = []
	for marble in marbles :
		for crownSecond in crownSeconds:
			if (crownSecond==marble):
				marbleInSecond.append(marble)
	return marbleInSecond


def advantage(state,symbol):
	me = marbleCount(state,symbol)
	you = marbleCount(state,mv.opponent(symbol))
	if me > you :
		return symbols[state['current']]
	elif you > me :
		return mv.opponent(symbols[state['current']])
	else : 
		return None

def valueOfState(state):
	advantage = marbleCount(state,mv.opponent(symbols[state['current']]))
	opponentNearBorder = len(findMarbleNearBorder(state,mv.opponent(symbols[state['current']])))
	opponentCrownSecond = len(findMarbleCrownSecond(state,mv.opponent(symbols[state['current']])))
	alliesCrownCenter = len(findMarbleCrownCenter(state,symbols[state['current']]))
	alliesNearBorder = len(findMarbleNearBorder(state,symbols[state['current']]))
	alliesCrownSecond = len(findMarbleCrownSecond(state,symbols[state['current']]))
	return {"advantage":advantage,"opponentNearBorder":opponentNearBorder,"opponentCrownSecond":opponentCrownSecond,"alliesCrownCenter":alliesCrownCenter,"alliesNearBorder":alliesNearBorder,"alliesCrownSecond":alliesCrownSecond}
	
def diff(previousState,nextState):
	previousAdvantage=previousState["advantage"]
	previousOpponentNearBorder=previousState["opponentNearBorder"]
	previousOpponentCrownSecond =previousState["opponentCrownSecond"]
	previousAlliesCrownCenter=previousState["alliesCrownCenter"]
	previousAlliesNearBorder=previousState["alliesNearBorder"]
	previousAlliesCrownSecond=previousState["alliesCrownSecond"]
	nextAdvantage=nextState["advantage"]
	nextOpponentNearBorder=nextState["opponentNearBorder"]
	nextOpponentCrownSecond =nextState["opponentCrownSecond"]
	nextAlliesCrownCenter=nextState["alliesCrownCenter"]
	nextAlliesNearBorder=nextState["alliesNearBorder"]
	nextAlliesCrownSecond=nextState["alliesCrownSecond"]
	value=0
	diff=0
	if previousAdvantage>nextAdvantage:
		diff = previousAdvantage - nextAdvantage
		value = value+diff*1000000
		if previousOpponentNearBorder< nextOpponentNearBorder :
			diff = nextOpponentNearBorder-previousOpponentNearBorder
			value = value + diff*500000
		if previousOpponentCrownSecond < nextOpponentCrownSecond :
			diff = nextOpponentCrownSecond-previousOpponentCrownSecond
			value = value + diff*50000
	else :
		
		if previousAlliesNearBorder > nextAlliesNearBorder:		
			diff = previousAlliesNearBorder - nextAlliesNearBorder
			value = value+diff*1000000
		else :
			diff = previousAlliesNearBorder - nextAlliesNearBorder
			value = value+diff*500000

		if previousOpponentCrownSecond < nextOpponentCrownSecond:
			diff = nextOpponentCrownSecond - previousOpponentCrownSecond
			value = value+diff*10000
		if previousAlliesCrownSecond > nextAlliesCrownSecond :
			diff =  previousAlliesCrownSecond- nextAlliesCrownSecond
			value = value+diff*1000
		else :
			diff =  previousAlliesCrownSecond- nextAlliesCrownSecond
			value = value+diff*500
		if previousAlliesCrownCenter < nextAlliesCrownCenter :
			diff =  nextAlliesCrownCenter- previousAlliesCrownCenter
			value = value+diff*100
		else :
			diff =  nextAlliesCrownCenter- previousAlliesCrownCenter
			value = value+diff*50
	return value


def valueOfMove(state,move,symbol):
	#compute current postion and give score to  the move
	def show(state):
		print('\n'.join([' '.join(line) for line in state['board']]))
		print()
	previousAdvantage = marbleCount(state,mv.opponent(symbols[state['current']]))
	previousOpponentNearBorder = len(findMarbleNearBorder(state,mv.opponent(symbols[state['current']])))
	previousOpponentCrownSecond = len(findMarbleCrownSecond(state,mv.opponent(symbols[state['current']])))
	previousAlliesCrownCenter = len(findMarbleCrownCenter(state,symbols[state['current']]))
	previousAlliesNearBorder = len(findMarbleNearBorder(state,symbols[state['current']]))
	previousAlliesCrownSecond = len(findMarbleCrownSecond(state,symbols[state['current']]))
	previousNeighbor = countNeighbor(state,symbols[state['current']])
	previousEliminationLine=0
	nextEliminationLine=0
	for marble in findMarbleNearBorder(state,symbols[state['current']]):
		previousEliminationLine=findEscape(state,marble)
	newState=mv.moveMarblesTrain(state,move[0],move[1])
	for marble in findMarbleNearBorder(newState,symbols[state['current']]):
		nextEliminationLine=findEscape(newState,marble)
	nextAdvantage = marbleCount(newState,mv.opponent(symbols[state['current']]))
	nextOpponentNearBorder = len(findMarbleNearBorder(newState,mv.opponent(symbols[state['current']])))
	nextOpponentCrownSecond = len(findMarbleCrownSecond(newState,mv.opponent(symbols[state['current']])))
	nextAlliesCrownCenter = len(findMarbleCrownCenter(newState,symbols[state['current']]))
	nextAlliesNearBorder = len(findMarbleNearBorder(newState,symbols[state['current']]))
	nextAlliesCrownSecond = len(findMarbleCrownSecond(newState,symbols[state['current']]))
	nextNeighbor = countNeighbor(state,symbols[state['current']])
	value = 0
	diff=0

	if previousAdvantage>nextAdvantage:
		diff = previousAdvantage - nextAdvantage
		value = value+diff*4000000
		if previousOpponentNearBorder< nextOpponentNearBorder :
			diff = nextOpponentNearBorder-previousOpponentNearBorder
			value = value + diff*1000000
		if previousOpponentCrownSecond < nextOpponentCrownSecond :
			diff = nextOpponentCrownSecond-previousOpponentCrownSecond
			value = value + diff*300000
		if nextNeighbor > previousNeighbor:
			diff =nextNeighbor-previousNeighbor
			value = value + 100*diff
	else :
		if previousAlliesNearBorder > nextAlliesNearBorder:		
			diff = previousAlliesNearBorder - nextAlliesNearBorder
			value = value+diff*4000000
		else :
			diff = previousAlliesNearBorder - nextAlliesNearBorder
			value = value+diff*500000
		if previousEliminationLine>nextEliminationLine:
			diff=previousEliminationLine-nextEliminationLine
			value = value+diff*100000
		if  previousOpponentNearBorder < nextOpponentNearBorder:
			diff =nextOpponentNearBorder - previousOpponentNearBorder
			value = value+diff*100000
		if previousOpponentCrownSecond <= nextOpponentCrownSecond:
			diff = nextOpponentCrownSecond - previousOpponentCrownSecond
			value = value+diff*10000
		if previousAlliesCrownSecond >= nextAlliesCrownSecond :
			diff =  previousAlliesCrownSecond- nextAlliesCrownSecond
			value = value+diff*1000
		else :
			diff =  previousAlliesCrownSecond- nextAlliesCrownSecond
			value = value+diff*500
		if nextNeighbor > previousNeighbor:
			diff =nextNeighbor-previousNeighbor
			value = value + 10*diff
		if previousAlliesCrownCenter < nextAlliesCrownCenter :
			diff =  nextAlliesCrownCenter- previousAlliesCrownCenter
			value = value+diff*100
		else :
			diff =  nextAlliesCrownCenter- previousAlliesCrownCenter
			value = value+diff*50	
	return value


def getBorderEscape():
	border=[[(0,0)],
			[(0,1),(0,2),(0,3)],
			[(0,4)],
			[(1,5),(2,6),(3,7)],
			[(4,8)],
			[(5,8),(6,8),(7,8)],
			[(8,8)],
			[(8,7),(8,6),(8,5)],
			[(8,4)],
			[(7,3),(6,2),(5,1)],
			[(4,0)],
			[(3,0),(2,0),(1,0)]]
	return border

def getEscapeDirection():
	escape =[['E','SE','SW'],
			['SE','SW'],
			['SE','SW','W'],
			['SW','W'],
			['SW','W','NW'],
			['W','NW'],
			['W','NW','NE'],
			['NW','NE'],
			['NW','NE','E'],
			['NE','E'],
			['SE','E','NE'],
			['E','SE']]
	return escape

def findEscape(state,marble):
	borders=getBorderEscape()
	eliminationDirection=getEscapeDirection()
	values=[]
	for i,border in enumerate(borders) :
		for positionBorder in border :
			if marble[0]==positionBorder[0] and marble[1]==positionBorder[1]:
				for direction in eliminationDirection[i]:
					value=0
					for i in range(1,3):
						pos = (marble[0]+directions[direction][0]*i,marble[1]+directions[direction][1]*i)
						if state["board"][pos[0]][pos[1]]==mv.opponent(symbols[state["current"]]):
							value=value+1
					values.append(value)
	return max(values)

if __name__=='__main__':
	state={'players': ['toto2', 'toto1'],
			'current': 1,
	  		'board': [['W', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X'],
	  			['W', 'E', 'E', 'E', 'E', 'E', 'X', 'X', 'X'],
	    		['E', 'B', 'E', 'E', 'E', 'E', 'E', 'X', 'X'],
		 		['E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'X'],
		 		['E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E'],
		   		['X', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
		    	['X', 'X', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
			 	['X', 'X', 'X', 'E', 'E', 'E', 'E', 'E', 'E'],
			  	['X', 'X', 'X', 'X', 'E', 'E', 'E', 'E', 'E']]
		}
	moves=[[[[1,0]], 'SW']]
	values=[]
	for i,move in enumerate(moves):
		values.append(valueOfMove(state,move,symbols[state['current']]))



		
		