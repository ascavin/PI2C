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

def isWinning(state,player):
	toCount = player
	count = 0
	for line in state['board']:
		for case in line:
			if case == toCount:
				count += 1
	if count<9:
		True
	return False

def winner(state):
	if isWinning(state,find.opponent(symbols[state['current']])) :
		return state['player'][state['current']]
	if isWinning(state,symbols[state['current']]) :
		return state['player'][state['current']]
	return None
	 

def utility(state, player):
	theWinner = winner(state)
	if theWinner is None:
		return 0
	if theWinner == player:
		return 1
	return -1

def gameOver(state):
	if winner(state) is not None:
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



def heuristic(state, player):
	res= efficiency.valueOfState(state)
	return res

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