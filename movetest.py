import gamestest as game

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

opposite = {
	'NE': 'SW',
	'SW': 'NE',
	'NW': 'SE',
	'SE': 'NW',
	'E': 'W',
	'W': 'E'
}

def getDirectionName(directionTuple):
	for dirName in directions:
		if directionTuple == directions[dirName]:
			return dirName
	raise game.BadMove('{} is not a direction'.format(directionTuple))

def computeAlignement(marbles):
	marbles = sorted(marbles, key=lambda L: L[0]*9+L[1])
	print(marbles)
	D = set()
	for i in range(len(marbles)-1):
		direction = (marbles[i+1][0]-marbles[i][0], marbles[i+1][1]-marbles[i][1])
		if direction not in directions.values():
			return None
		D.add(direction)
	return getDirectionName(D.pop()) if len(D) == 1 else None

def checkMarbles(state, move):
	marbles = move['marbles']
	color = symbols[state['current']]
	if not 0 <= len(marbles) < 4:
		raise game.BadMove('You can only move 1, 2, or 3 marbles')

	for pos in marbles:
		if getColor(state, pos) != color:
			raise game.BadMove('Marble {} is not yours'.format(pos))
		
def isOnBoard(pos):
	l, c = pos
	if min(pos) < 0:
		return False
	if max(pos) > 8:
		return False
	if abs(c-l) >= 5:
		return False
	return True

def addDirection(pos, direction):
	D = directions[direction]
	return (pos[0] + D[0], pos[1] + D[1])

def moveOneMarble(state, pos, direction):
	li, ci = pos
	ld, cd = addDirection(pos, direction)
	color = getColor(state, pos)
	try:
		destStatus = getStatus(state, (ld, cd))
	except:
		destStatus = 'X'
	
	if color != 'W' and color != 'B':
		raise game.BadMove('There is no marble here {}'.format(pos))
	if destStatus == 'W' or destStatus == 'B':
		raise game.BadMove('There is already a marble here {}'.format((ld, cd)))
	
	res = copy.copy(state)
	res['board'] = copy.copy(res['board'])
	res['board'][li] = copy.copy(res['board'][li])
	res['board'][li][ci] = 'E'

	if destStatus == 'E':
		res['board'][ld] = copy.copy(res['board'][ld])
		res['board'][ld][cd] = color

	return res

def opponent(color):
	if color == 'W':
		return 'B'
	return 'W'

def getStatus(state, pos):
	if not isOnBoard(pos):
		raise game.BadMove('The position {} is outside the board'.format(pos))
	return state['board'][pos[0]][pos[1]]

def isEmpty(state, pos):
	return getStatus(state, pos) == 'E'

def isFree(state, pos):
	if isOnBoard(pos):
		return isEmpty(state, pos)
	else:
		return True

def getColor(state, pos):
	status = getStatus(state, pos)
	if status == 'W' or status == 'B':
		return status
	raise game.BadMove('There is no marble here {}'.format(pos))

def moveMarblesTrain(state, marbles, direction):
	if direction in ['E', 'SE', 'SW']:
		marbles = sorted(marbles, key=lambda L: -(L[0]*9+L[1]))
	else:
		marbles = sorted(marbles, key=lambda L: L[0]*9+L[1])

	color = getColor(state, marbles[0])

	pos = addDirection(marbles[0], direction)
	toPush = []
	while not isFree(state, pos):
		if getColor(state, pos) == color:
			raise game.BadMove('You can\'t push your own marble')
		toPush.append(pos)
		pos = addDirection(pos, direction)

	if len(toPush) >= len(marbles):
		raise game.BadMove('you can\'t push {} opponent\'s marbles with {} marbles'.format(len(toPush), len(marbles)))

	state = moveMarbles(state, list(reversed(toPush)) + marbles, direction)

	return state

def moveMarbles(state, marbles, direction):
	for pos in marbles:
		state = moveOneMarble(state, pos, direction)
	return state

def sameLine(direction1, direction2):
	if direction1 == direction2:
		return True
	if direction1 == opposite[direction2]:
		return True
	return False

def isWinning(state):
	toCount = opponent(symbols[state['current']])
	count = 0
	for line in state['board']:
		for case in line:
			if case == toCount:
				count += 1
	return count < 9



     
                 



def Abalone(players):
	if len(players) != 2:
		raise game.BadGameInit('Tic Tac Toe must be played by 2 players')

	state = {
		'players': players,
		'current': 0,
		'board': [
			['W', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X'],
			['W', 'W', 'W', 'W', 'W', 'W', 'X', 'X', 'X'],
			['E', 'E', 'W', 'W', 'W', 'E', 'E', 'X', 'X'],
			['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'X'],
			['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
			['X', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
			['X', 'X', 'E', 'E', 'B', 'B', 'B', 'E', 'E'],
			['X', 'X', 'X', 'B', 'B', 'B', 'B', 'B', 'B'],
			['X', 'X', 'X', 'X', 'B', 'B', 'B', 'B', 'B']
		]
	}

	# move = {
	# 	'marbles': [],
	# 	'direction': ''
	# }

	def next(state, move):
		if move is None:
			raise game.BadMove('None is not a valid move')

		checkMarbles(state, move)
		marbles = move['marbles']

		if len(marbles) != 0:
			marblesDir = computeAlignement(marbles)
			if marblesDir is None and len(marbles) > 1:
				raise game.BadMove('The marbles you want to move must be aligned')

			if len(marbles) == 1:
				state = moveOneMarble(state, marbles[0], move['direction'])
			elif sameLine(move['direction'], marblesDir):
				state = moveMarblesTrain(state, marbles, move['direction'])
			else:
				state = moveMarbles(state, marbles, move['direction'])

			if isWinning(state):
				raise game.GameWin(state['current'], state)
		
		state['current'] = (state['current'] + 1) % 2
		return state

	return state, next


def isAdvantage(state):
	Opponent = opponent(symbols[state['current']])
	MySelf = symbols[state['current']]
	countOpponent = 0
	countMySelf=0
	for line in state['board']:
		for case in line:
			if case == Opponent:
				countOpponent += 1
			if case == MySelf:
				countMySelf += 1
	if countMySelf > countOpponent :
		return 1
	elif countMySelf==countOpponent :
		return None
	return 0

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

class isPossibleTo:
    def __init__(self):
       pass 
    def moveManyMarbles():
        return False

    def aMarblesNextToAllies():
        return False

    def moveOpponentMarbleOutOfTheBoard():
        return False


def move(state, player):
    ask = isPossibleTo()
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

def findMarbleNearBorder():
	border=[(0,0),
			(0,1),
			(0,2),
			(0,3),
			(0,4),
			(1,5),
			(2,6),
			(2,3),
			(1,0),
			(2,0),
			(3,0),
			(4,0),
			]

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
#                           Yes : Try to go next to a neighbour select the marbles with the most marbles neighbours 'allies'
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


    for line in state['board']:
        for column in line:







Game = Abalone

if __name__=='__main__':
	def show(state):
		print('\n'.join([' '.join(line) for line in state['board']]))
		print()

	state, next = Abalone(['LUR', 'LRG'])

	state['board'][3][3] = 'B'
	state['board'][4][3] = 'W'

	show(state)

	state = moveMarblesTrain(state, [(0,0),(1,1),(2,2)], 'SE')
	show(state)
	#state = moveMarblesTrain(state, [(1, 3), (2, 3), (3, 3)], 'SW')
	#show(state)
	#state = moveMarblesTrain(state, [(2, 3), (3, 3), (4, 3)], 'SW')
	#show(state)
	#state = moveMarblesTrain(state, [(3, 3), (4, 3), (5, 3)], 'SW')
	#show(state)
