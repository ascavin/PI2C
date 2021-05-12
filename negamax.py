from collections import defaultdict
import random
import time 
import move as find
import find_move as rs
import efficiency

state = [ 
    None,None,None,
    None,None,None,
    None,None,None,
]
lines = [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8],
	[0, 3, 6],
	[1, 4, 7],
	[2, 5, 8],
	[0, 4, 8],
	[2, 4, 6]
]
symbols = ['B', 'W']
	 

def utility(state, player):
	theWinner = find.winner(state)
	if theWinner is None:
		return 0
	if theWinner == player:
		return 1
	return -1

def gameOver(state):
	if find.winner(state) is not None:
		return True
	else : 
		return False

def currentPlayer(state):
	return state['player'][state['current']]

def moves(state):               
	def getMarbleLocation(state,symbol):
		locations=[] 
		for i,line in enumerate(state['board']):
			for e,column in enumerate(line) :
				if (state['board'][i][e]==symbol):
					locations.append((i,e))
		return locations
	#print("in moves symbol",symbols[state['current']])
	marbles = getMarbleLocation(state,symbols[state['current']])
	allMoves=[]
	moves_marble=[]
	for marble in marbles:
		moves_marble = rs.findMove(state['board'],marble,symbols[state['current']])
		for elem in moves_marble:		
			allMoves.append(elem)
	return allMoves

def apply(state, move):            #to change state of grid use apply
	res=find.moveMarblesTrain(state,move[0],move[1])
	return res

def timeit(fun):
	def wrapper(*args, **kwargs):
		start = time.time()
		res = fun(*args, **kwargs)
		print('Executed in {}s'.format(time.time() - start))
		return res
	return wrapper

@timeit
def next(state,fun):
	player = currentPlayer(state)
	_, move = fun(state, player)
	return move




from collections import defaultdict

def negamaxWithPruningIterativeDeepening(state, player, timeout=0.2):
	#print('compute')
	cache = defaultdict(lambda : 0)
	def cachedNegamaxWithPruningLimitedDepth(state, player, depth, alpha=float('-inf'), beta=float('inf')):
		#print('compute')
		over = gameOver(state)
		if over or depth == 0:		
			res = -heuristic(state, player), None, over
			print(res)

		else:
			theValue, theMove, theOver = float('-inf'), None, True
			possibilities = [(move, apply(state, move)) for move in moves(state)]
			possibilities.sort(key=lambda poss: cache[tuple(poss[1])])
			for move, successor in reversed(possibilities):
				value, _, over = cachedNegamaxWithPruningLimitedDepth(successor, player%2+1, depth-1, -beta, -alpha)
				theOver = theOver and over
				if value > theValue:
					theValue, theMove = value, move
				alpha = max(alpha, theValue)
				if alpha >= beta:
					break
			res = -theValue, theMove, theOver
		cache[tuple(state)] = res[0]
		return res

	value, move = 0, None
	depth = 1
	start = time.time()
	over = False
	while time.time() - start < timeout and not over:
		value, move, over = cachedNegamaxWithPruningLimitedDepth(state, player, depth)
		depth += 1

	print(value, move)
	return value, move

def run(state):
	result=[]
	allMoves=moves(state)
	newStates=[]
	M=find.opponent(symbols[state['current']])
	for move in allMoves:
		print(move)
		previous=0
		nextstep=0
		newState=find.moveMarblesTrain(state,move[0],move[1])
		for i,line in enumerate(state['board']):
			for e,column in enumerate(line):
				if state['board'][i][e]==M:
					previous=previous+1
		for i,line in enumerate(newState['board']):
			for e,column in enumerate(line):
				if newState['board'][i][e]==M:
					nextstep=nextstep+1
		if nextstep<previous:
			result={"response": "move",
			"move": {'marbles':move[0][0],'direction':move[0][1]},
			"message": "pass"}
			return result
		else :
			newStates.append(newState)
	print("-------------")	
	nextMove=random.sample(allMoves,1)
	print(nextMove)
	print("next",nextMove)
	result={"response": "move",
	"move": {'marbles':nextMove[0][0],'direction':nextMove[0][1]},
	"message": "pass"}
	return result


def random1(state):
	def getMarbleLocation(state,symbol):
		locations=[] 
		for i,line in enumerate(state['board']):
			for e,column in enumerate(line) :
				if (state['board'][i][e]==symbol):
					locations.append((i,e))
		return locations
	marbles = getMarbleLocation(state,symbols[state['current']])
	allMoves=[]
	moves_marble=[]
	for marble in marbles:
		moves_marble = rs.findMove(state['board'],marble,symbols[state['current']])
		for elem in moves_marble:		
			allMoves.append(elem)
	nextMove=random.sample(allMoves,1)
	print(nextMove)
	result={"response": "move",
	"move": {'marbles':nextMove[0][0],'direction':nextMove[0][1]},
	"message": "pass"}
	return result
	

def think(state):
	def getMarbleLocation(state,symbol):
		locations=[] 
		for i,line in enumerate(state['board']):
			for e,column in enumerate(line) :
				if (state['board'][i][e]==symbol):
					locations.append((i,e))
		return locations
	marbles = getMarbleLocation(state,symbols[state['current']])
	allMoves=[]
	moves_marble=[]
	for marble in marbles:
		moves_marble = rs.findMove(state['board'],marble,symbols[state['current']])
		for elem in moves_marble:		
			allMoves.append(elem)
	values=[]
	for move in allMoves:
		values.append(efficiency.valueOfMove(state,move,symbols[state['current']]))
	choice=max(values)
	moves=[]
	for i,value in enumerate(values) :
		if value == choice :
			moves.append(allMoves[i])
	nextMove=random.sample(moves,1)
	print(nextMove)
	result={"response": "move",
	"move": {'marbles':nextMove[0][0],'direction':nextMove[0][1]},
	"message": "pass"}
	return result
	
		

def bin(state):
	def getMarbleLocation(state,symbol):
		locations=[] 
		for i,line in enumerate(state['board']):
			for e,column in enumerate(line) :
				if (state['board'][i][e]==symbol):
					locations.append((i,e))
		return locations
	marbles = getMarbleLocation(state,symbols[state['current']])
	allMoves=[]
	moves_marble=[]
	for marble in marbles:
		moves_marble = rs.findMove(state['board'],marble,symbols[state['current']])
		for elem in moves_marble:		
			allMoves.append(elem)
	print(allMoves)
	M=symbols[state['current']]
	goodMoves=[]
	for move in allMoves:
		previous=0
		nextstep=0
		newState=find.moveMarblesTrain(state,move[0],move[1])
		for i,line in enumerate(state['board']):
			for e,column in enumerate(line):
				if state['board'][i][e]==M:
					previous=previous+1
		for i,line in enumerate(newState['board']):
			for e,column in enumerate(line):
				if newState['board'][i][e]==M:
					nextstep=nextstep+1
		if nextstep==previous:
			goodMoves.append(move)
	print(goodMoves)	
	nextMove=random.sample(goodMoves,1)
	print("next",nextMove)
	result={"response": "move",
	"move": {'marbles':nextMove[0][0],'direction':nextMove[0][1]},
	"message": "pass"}
	return result

def bestMove(state):
	ties0 = possibilities(state)
	ties1 =[]
	ties2 =[]
	ties3 =[]
	for tie in ties0:
		ties1.append(possibilities(tie[0]))
	for tie in ties1:
		ties2.append(possibilities(tie[0]))
	for tie in ties2:
		ties3.append(possibilities(tie[0]))
	values=[]
	for tie0 in ties0:
		for tie1 in ties1:
			for tie2 in ties2:
				for tie3 in ties3:
					value = tie0[2] + tie1[2] +tie2[2] +tie3[2]
					values.append(value)
	choice=max(values)
	for tie0 in ties0:
		for tie1 in ties1:
			for tie2 in ties2:
				for tie3 in ties3:
					value = tie0[2] + tie1[2] +tie2[2] +tie3[2]
					if value == choice : 
						move=tie0[1]
	result={"response": "move",
	"move": {'marbles':move[0],'direction':move[1]},
	"message": "pass"}
	return result

def possibilities(state):
	def getMarbleLocation(state,symbol):
		locations=[] 
		for i,line in enumerate(state['board']):
			for e,column in enumerate(line) :
				if (state['board'][i][e]==symbol):
					locations.append((i,e))
		return locations
	marbles = getMarbleLocation(state,symbols[state['current']])
	allMoves=[]
	moves_marble=[]
	for marble in marbles:
		moves_marble = rs.findMove(state['board'],marble,symbols[state['current']])
		for elem in moves_marble:		
			allMoves.append(elem)
	result=[]
	for move in allMoves:
		newState,value = efficiency.valueOfMove(state,move,symbols[state['current']])
		savingData  = [newState, move, value]
		result.append(savingData)
	return result
	
def MinMax(state,depth):
	if (find.winner(state) or depth <= 0) :
		#print("stop")
		return efficiency.valueOfState(state),None

	if (state["current"]==0):
		bestScore=float("-inf")
		allMoves=moves(state)
		for move in allMoves:
			#value=efficiency.valueOfMove(state,move,state["current"])
			nextState=apply(state,move)
			state["current"]=1
			depth=depth-1
			#print("max",depth)
			value,_ = MinMax(nextState,depth)
			if value > bestScore :
				bestScore=value
				bestMove =move
	else :
		bestScore=float("inf")
		allMoves=moves(state)
		for move in allMoves:
			#value=efficiency.valueOfMove(state,move,state["current"])
			nextState=apply(state,move)
			state["current"]=0
			depth=depth-1
			#print("min",depth)
			value,_ = MinMax(nextState,depth)
			if value < bestScore :
				bestScore=value
				bestMove =move
	return bestScore,bestMove


def heuristic(state):
	if gameOver(state):
		theWinner = find.winner(state)
		if theWinner is None:
			return 0
		if theWinner == state['player'][state['current']]:
			return 100000
		if theWinner == state['player'][state['current']]%2+1:
			return -100000
	res = efficiency.valueOfState(state)
	return res
	
def negamaxWithPruningLimitedDepth(state, player, depth=4, alpha=float('-inf'), beta=float('inf')):
	if gameOver(state) or depth == 0:
		return -heuristic(state), None

	theValue, theMove = float('-inf'), None
	for move in moves(state):
		successor = apply(state, move)
		value, _ = negamaxWithPruningLimitedDepth(successor, state["current"]%2+1, depth-1, -beta, -alpha)
		if value > theValue:
			theValue, theMove = value, move
		alpha = max(alpha, theValue)
		if alpha >= beta:
			break
	return -theValue, theMove

if __name__=='__main__':
	state={'players': ['toto2', 'toto1'],
			'current': 0,
	  		'board': [['W', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X'],
	  			['W', 'W', 'W', 'W', 'W', 'W', 'X', 'X', 'X'],
	    		['E', 'E', 'W', 'W', 'W', 'E', 'E', 'X', 'X'],
		 		['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'X'],
		 		['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
		   		['X', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E'],
		    	['X', 'X', 'E', 'E', 'B', 'B', 'B', 'E', 'E'],
			 	['X', 'X', 'X', 'B', 'B', 'B', 'B', 'B', 'B'],
			  	['X', 'X', 'X', 'X', 'B', 'B', 'B', 'B', 'B']]
		}
	result=MinMax(state,3)
	print(result)

################################################################################################


def evaluate(state):
	return False 

def getAllPieces(state,symbol):
	locations=[] 
	for i,line in enumerate(state['board']):
		for e,column in enumerate(line) :
			if (state['board'][i][e]==symbol):
				locations.append((i,e))
	return locations

def aiMove(state,marbles,move):
	return False

from copy import deepcopy

global depth
global tree

def climb(state,depth):
	depth=0
	player=0
	while depth<3:
		movesValue=evaluateMove(state,player)
		tree.append(movesValues)
		currentDepth=currentDepth+1
		for move in movesValue :
			climb(move[0],depth)


def evaluateMove(state,player):
	for move in getAllMoves(state, currentPlayer):
		valuesPreviousState=efficiency.valueOfState(state)
		newState={"player":deepcopy(state["player"]),"current":deepcopy(state["current"]),"board":deepcopy(state['board'])}
		newState=apply(newState,move)
		valuesNextState=efficiency.valueOfState(newState)
		value = efficiency.diff(valuesPreviousState,valuesNextState)
		allMoves.append([newState,move,value])
	return allMoves




#def minimax(state,maxPlayer):
#
#		return maxEval, bestmove
#	else:
#		minEval=float('inf')
#		best_move = None 
#		for move in getAllMoves(state, currentPlayer,game):
#			evaluation = minimax(move,depth-1,True,game)[0]
#			minEval=min(inEval,evaluation)
#			if minEval==evaluation:
#				bestMove=move
#		return maxEval, bestmove

def getAllMoves(state, currentPlayer):
	marbles = getMarbleLocation(state,symbols[state['current']])
	allMoves=[]
	for marble in marbles:
		movesMarble = rs.findMove(state['board'],marble,symbols[state['current']])
		for move in movesMarble:
			newState={"player":deepcopy(state["player"]),"current":deepcopy(state["current"]),"board":deepcopy(state['board'])}
			newBoard=apply(newState,move)
			allMoves.append(newState,move)
	return allMoves

