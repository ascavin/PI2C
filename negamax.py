from collections import defaultdict
import random
import time 
import move as find

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
	res = []
	def getMarbleLocation(state,symbol):
		locations=[] 
		for i,line in enumerate(state['board']):
			for e,column in enumerate(line) :
				if (state['board'][i][e]==symbol):
					locations.append((i,e))
		return locations
	marbles = getMarbleLocation(state,symbols[state['current']])
	moves=[]
	print(marbles)
	for marble in marbles:
		moveschoices=find.move2Marbleispossible(state,marble)
		if moveschoices[0]==True:
			print(moveschoices)
			break
	# 		directions=list(moveschoices[1].keys())
	# 		moves.append({marble:directions})
	# position=random.choice(moves)
	# for key in position:
	# 	p=key
	# 	d=position[key]
	# direction=random.sample(d,1)
	# result={"response": "move",
	# "move": {'marbles':[[p[0],p[1]]],'direction':direction[0]},
	# "message": "Fun message"}
	return res

def apply(state, move):            #to change state of grid use apply
	player = currentPlayer(state)
	res=[]
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

def show(state):
	state = [
            'X' if val == 1 else 
			'O' if val == 2 else 
			' ' for val in state]
	print(state[:3])
	print(state[3:6])
	print(state[6:])
	print()

def lineValue(line, player):
	counters = {
		1: 0,
		2: 0,
		None: 0
	}

	for elem in line:
		counters[elem] += 1

	if counters[player] > counters[player%2+1]:
		return 1
	if counters[player] == counters[player%2+1]:
		return 0
	return -1


def heuristic(state, player):
	if gameOver(state):
		theWinner = winner(state)
		if theWinner is None:
			return 0
		if theWinner == player:
			return 9
		return -9
	res = 0
	for line in lines:
		res += lineValue([state[i] for i in line], player)
	return res

from collections import defaultdict

def negamaxWithPruningIterativeDeepening(state, player, timeout=0.2):
	cache = defaultdict(lambda : 0)
	def cachedNegamaxWithPruningLimitedDepth(state, player, depth, alpha=float('-inf'), beta=float('inf')):
		over = gameOver(state)
		if over or depth == 0:
			res = -heuristic(state, player), None, over

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
	while value > -9 and time.time() - start < timeout and not over:
		value, move, over = cachedNegamaxWithPruningLimitedDepth(state, player, depth)
		depth += 1

	print('depth =', depth)
	return value, move


def run(state):
	result=[]
	moves
	return result




