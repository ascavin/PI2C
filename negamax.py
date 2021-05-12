from collections import defaultdict
import random
import time 
import move
import find_move as rs
import efficiency

symbols = ['B', 'W']

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


def winner(state):
	if move.isWinning(state,move.opponent(symbols[state['current']])) :
		return state['player'][state['current']]
	if move.isWinning(state,symbols[state['current']]) :
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
	res=move.moveMarblesTrain(state,move[0],move[1])
	return res

#but : partir de l'etat gagnant du joueur et remonter jusqu'a l'etat initial du jeu pour pouvoir selectionner
# les moves qui vont nous permettre de gagner

def MAX(state, player):#allie
	if gameOver(state):
		return utility(state, player), None

	theValue, theMove = float('-inf'), None
	for move in moves(state):#parmis tout les mouvements possibles au départ 
		#print("move",move)
		newState = apply(state, move) # jouer chaque mouvement et garder en memoire le mvt joue 
		value, _ = MIN(newState, player)# au tour du joueur adverse de jouer (calcul des coups possibles du joueur adverses et retourne son meilleur coup pour gagner)
		if value > theValue:
			theValue, theMove = value, move
	return theValue, theMove



def MIN(state, player):#adversaire
	if gameOver(state):
		return utility(state, player), None

	theValue, theMove = float('inf'), None
	for move in moves(state):#parmis tout les mouvements possibles au départ
		newState = apply(state, move)# jouer chaque mouvement et garder en memoire le mvt joue 
		value, _ = MAX(newState, player)# au tour du joueur adverse de jouer (calcul des coups possibles du joueur adverses et retourne son meilleur coup pour gagner)
		if value < theValue:
			theValue, theMove = value, move
	return theValue, theMove

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
			#print(res)

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

	#print(value, move)
	return value, move

def run(state):
	result=[]
	allMoves=moves(state)
	newStates=[]
	M=move.opponent(symbols[state['current']])
	for move in allMoves:
		#print(move)
		previous=0
		nextstep=0
		newState=move.moveMarblesTrain(state,move[0],move[1])
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
	#print("-------------")	
	nextMove=random.sample(allMoves,1)
	#print(nextMove)
	#print("next",nextMove)
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
	#print(nextMove)
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
	#print(nextMove)
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
	#print(allMoves)
	M=symbols[state['current']]
	goodMoves=[]
	for move in allMoves:
		previous=0
		nextstep=0
		newState=move.moveMarblesTrain(state,move[0],move[1])
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
	#print(goodMoves)	
	nextMove=random.sample(goodMoves,1)
	#print("next",nextMove)
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
	
		
if (__name__=="__main__"):
	
	state, next = move.Abalone(["jojo","jack"])

	def show(state):
		print('\n'.join([' '.join(line) for line in state]))
		print()
	show(state['board'])
	print("moves available",moves(state))
	print(MAX(state, state['current']))