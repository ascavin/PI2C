import gamestest as game
import copy

symbols = ['B', 'W']# symbols of players ; 'white marbles' and 'black marbles'

directions = {
	'NE': (-1,  0),
	'SW': ( 1,  0),
	'NW': (-1, -1),
	'SE': ( 1,  1),
	 'E': ( 0,  1),
	 'W': ( 0, -1)
}# directions possible on the abalone board

opposite = {
	'NE': 'SW',
	'SW': 'NE',
	'NW': 'SE',
	'SE': 'NW',
	'E': 'W',
	'W': 'E'
}# opposite of each directions


def getDirectionName(directionTuple):# return the name of the direction associate with location move 
	for dirName in directions:
		if directionTuple == directions[dirName]:
			return dirName
	raise game.BadMove('{} is not a direction'.format(directionTuple))

def computeAlignement(marbles):
	marbles = sorted(marbles, key=lambda L: L[0]*9+L[1])
	D = set()
	for i in range(len(marbles)-1):
		direction = (marbles[i+1][0]-marbles[i][0], marbles[i+1][1]-marbles[i][1])
		if direction not in directions.values():
			return None
		D.add(direction)
	return getDirectionName(D.pop()) if len(D) == 1 else None

def checkMarbles(state, move):
	if 'marbles' not in move:
		raise game.BadMove('The move do not contains the marbles key')
	marbles = move['marbles']
	color = symbols[state['current']]
	if not 0 <= len(marbles) < 4:
		raise game.BadMove('You can only move 1, 2, or 3 marbles')

	for pos in marbles:
		if getColor(state, pos) != color:
			raise game.BadMove('Marble {} is not yours'.format(pos))
		
def isOnBoard(pos):#is the marble on the board
	l, c = pos
	if min(pos) < 0:
		return False
	if max(pos) > 8:
		return False
	if abs(c-l) >= 5:
		return False
	return True

def addDirection(pos, direction):# moving of one case from the 'pos' location to an other selected by direction 
	D = directions[direction]
	return (pos[0] + D[0], pos[1] + D[1])

def moveOneMarble(state, pos, direction):# is for moving a marble 
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

def opponent(color):# return the symbol of the opponent player
	if color == 'W':
		return 'B'
	return 'W'

def getStatus(state, pos):# get the status of a case on the board and return 'E' or 'W' or 'B'
	if not isOnBoard(pos):
		raise game.BadMove('The position {} is outside the board'.format(pos))
	return state['board'][pos[0]][pos[1]]

def getStatusgrid(state, pos):# get the status of a case on the board and return 'E' or 'W' or 'B' directly on the grid
	if not isOnBoard(pos):
		raise game.BadMove('The position {} is outside the board'.format(pos))
	return state[pos[0]][pos[1]]

def isEmpty(state, pos):#check if a case is empty
	return getStatus(state, pos) == 'E'

def isFree(state, pos):#check if a case is available
	if isOnBoard(pos):
		return isEmpty(state, pos)
	else:
		return True

def getColor(state, pos):#return the color of the player on the 'pos' location
	status = getStatus(state, pos)
	if status == 'W' or status == 'B':
		return status
	raise game.BadMove('There is no marble here {}'.format(pos))

def moveMarblesTrain(state, marbles, direction):#move more than 1 marble
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

def moveMarbles(state, marbles, direction):#for moving many marbles 
	for pos in marbles:
		state = moveOneMarble(state, pos, direction)
	return state

def sameLine(direction1, direction2):# check if directions of marbles are the same or opposite to find an alignment 
	if direction1 == direction2:
		return True
	if direction1 == opposite[direction2]:
		return True
	return False

def isWinning(state):# check if there is a winner in the game (if there is 6 marbles of a player out)
	toCount = opponent(symbols[state['current']])
	count = 0
	for line in state['board']:
		for case in line:
			if case == toCount:
				count += 1
	return count < 9

def winner(state):# return the winner 
	if isWinning(state,opponent(symbols[state['current']])) :
		return state['player'][state['current']]
	if isWinning(state,symbols[state['current']]) :
		return state['player'][state['current']]
	return None

def Abalone(players):# return the board with the players and the current player
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

	def next(state, move):
		if move is None:
			raise game.BadMove('None is not a valid move')

		checkMarbles(state, move)
		marbles = move['marbles']

		if 'direction' not in move:
			raise game.BadMove('The move do not contains the direction key')

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


def findMove(grid,marble,symbol):# check all moves (sumito,line) available for a marble (or 2 or 3) of a player 
	moves=[]#initialize moves 
	alignement=[]#initialize alignment
	possibilities=[]#initialize possibilities
	for direction in directions :#for each direction
		#print('test diretion :',direction)
		find=True
		e=1        #elements number of the alignment
		alignement.clear()
		while find and e<6:           
			#print("neighbor",(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e),insidetheboard(grid,(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e)))
			#print(alignement.append(insidetheboard(grid,(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e))))
			alignement.append(insidetheboard(grid,(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e)))
			possibilities=getPossibilities(symbol)
			#print(alignement)
			for i,possibilitie in enumerate(possibilities):
				if possibilitie == alignement :	
					#print(possibilitie)
					#print(alignement)	
					m1 = [marble[0],marble[1]]#marble1
					m2 = [marble[0]+directions[direction][0],marble[1]+directions[direction][1]]#marble2, next to marble1
					m3 = [marble[0]+directions[direction][0]*2,marble[1]+directions[direction][1]*2]#marble3, next to marble2							
					find=False
										
					if i == 0: #if the next position after m1 is empty
						#print("0")
						moves.append([[m1],direction])				
					#if i == 1:
						#print("1")
					if i == 2: #if the next position after m1 is an m2 allie marble and if the next possible after m2 is empty
						#print("2")
						moves.append([[m1,m2],direction])
						sumito2m(grid,m1,m2,moves,direction)
					if i==3:#if the next position after m1 is an m2 allie marble and if the next possible after m2 is outside the board
						#print("3")
						sumito2m(grid,m1,m2,moves,direction)
					if i == 4:#if the next position after m1 is an m2 allie marble and if the next position after m2 is an m3 allie marble and if the next possible after m2 is empty
						#print("4")
						moves.append([[m1,m2,m3],direction])
						sumito3m(grid,m1,m2,m3,moves,direction)
							
					if i == 5:#if the next position after m1 is an m2 allie marble, if the next position after m2 is an m3 allie marble and  if the next possible after m3 is outside the board
						#print("5")
						sumito3m(grid,m1,m2,m3,moves,direction)
					if (i == 6):#if the next position after m1 is an m2 allie marble, if the next position after m2 is an m3 opponent marble and  if the next possible after m3 is empty
						moves.append([[m1,m2],direction])
						sumito2m(grid,m1,m2,moves,direction)
						#print("6")
					if i == 7:#if the next position after m1 is an m2 allie marble, if the next position after m2 is an m3 opponent marble and  if the next possible after m3 is outside the board
						#print("7")
						moves.append([[m1,m2],direction])
						sumito2m(grid,m1,m2,moves,direction)	
								
					if i == 8:#if the next position after m1 is an m2 opponent marble, if the next position after m2 is an m3 opponent marble 
						#print("8")
						sumito2m(grid,m1,m2,moves,direction)
					if i == 9:#if the next position after m1 is an m2 allie marble, if the next position after m2 is an m3 allie marble and if the next position after m3 is an m4 allie marble
						#print("9")
						sumito3m(grid,m1,m2,m3,moves,direction)
					if i == 10 or i==11:#if the next position after m1 is an m2 allie marble, if the next position after m2 is an m3 allie marble and if the next position after m3 is an m4 opponent marble and next location is empty or outside
						#print("10 et 11")
						moves.append([[m1,m2,m3],direction])
						sumito3m(grid,m1,m2,m3,moves,direction)
 
						#print("ok")

					if i == 12 or i==13:#if the next position after m1 is an m2 allie marble, if the next position after m2 is an m3 allie marble, if the next position after m3 is an m4 opponent marble,if the next position after m4 is an m5 opponent marble  and next location is empty or outside
						#print("12 et 13")
						moves.append([[m1,m2,m3],direction])
						sumito3m(grid,m1,m2,m3,moves,direction)
						
					if i == 14:#if the next position after m1 is an m2 allie marble, if the next position after m2 is an m3 allie marble, if the next position after m3 is an m4 opponent marble,if the next position after m4 is an m5 opponent marble and if the next position after m5 is an m6 opponent marble  
						#print("14")
						sumito3m(grid,m1,m2,m3,moves,direction)
						pass


					break


			e=e+1   
	return moves

			
def insidetheboard(grid,marble):#check if the marble is inside the board , otherwise , it returns 'X' for outside location
	li,ci = marble
	#print(marble)
	if  (0<=li<=4 and 0<=ci<=4) or (5<=li<=8 and 5<=ci<=8) or (5<=li<=8 and 0<=ci<=4 and not grid[li][ci] == 'X') or (0<=li<=4 and 5<=ci<=8 and not grid[li][ci] == 'X'):
		res=grid[marble[0]][marble[1]]

		return res
	else : 
		return 'X'

def isonboard(grid,marble):#boolean version of the insidetheboard function
	li,ci = marble
	if  (0<=li<=4 and 0<=ci<=4) or (5<=li<=8 and 5<=ci<=8) or (5<=li<=8 and 0<=ci<=4 and not grid[li][ci] == 'X') or (0<=li<=4 and 5<=ci<=8 and not grid[li][ci] == 'X'):
		return True
	else :
		return False 

def getPossibilities(symbol):#return all movement possible on abalone board according to the rules of the game         
	possibilities =[
					['E'],                 				#:True,    #0    
					['X'],								#:False		#1
					[symbol,'E'],            			 #:True,    #2    possible sumito
					[symbol,'X'],						#False,		#3		possible sumito
					[symbol,symbol,'E'],         			#:True,    #4    possible sumito
					[symbol,symbol,'X'],					#False,		#5	possible sumito
					[symbol,opponent(symbol),'E'],        			#:True,    #6    #je sors une bille adverse		possible sumito
					[symbol,opponent(symbol),'X'],					#:True 		#7														possible sumito
					[symbol,opponent(symbol),opponent(symbol)],        					#:False,   #8    #je ne peux pas bouger			possible sumito
					[symbol,symbol,symbol],        					 					#:False,   #9    #je ne peux pas bouger			possible sumito
					[symbol,symbol,opponent(symbol),'E'],     							#:True,    #10    #je sors une bille adverse	possible sumito
					[symbol,symbol,opponent(symbol),'X'],								#:True, 	#11									possible sumito
					[symbol,symbol,opponent(symbol),opponent(symbol),'E'], 				#:True,    #12    #je sors une bille adverse	possible sumito
					[symbol,symbol,opponent(symbol),opponent(symbol),'X'],				#:True 		#13									possible sumito
					[symbol,symbol,opponent(symbol),opponent(symbol),opponent(symbol)], #:False,   #14    #je ne peux pas bouger		possible sumito
					]

	return possibilities

def sumito3m(grid,m1,m2,m3,moves,direction):# function for sumito of 3 marbles
	directionlist = []
	for elem in [m1,m2,m3]:#for each marble
		for eachdirection in directions :#for each direction
			#print(direction)
			if eachdirection == direction or eachdirection == opposite[direction]:
				pass
			else:# directions de lalignement exclu
				if isonboard(grid,addDirection(elem, eachdirection)):
					if getStatusgrid(grid,addDirection(elem, eachdirection)) == 'E':
						directionlist.append(eachdirection)
						#print(directionlist)
	for i in directions:
		if directionlist.count(i) == 3 :
			moves.append([[m1,m2,m3],i])
			pass	
	directionlist.clear()
	return None

def sumito2m(grid,m1,m2,moves,direction):# function for sumito of 2 marbles
	directionlist = []
	for elem in [m1,m2]:#for each marble
		for eachdirection in directions :#for each direction
			#print(direction)
			if eachdirection == direction or eachdirection == opposite[direction]:
				pass
			else:# directions de lalignement exclu
				if isonboard(grid,addDirection(elem, eachdirection)):
					if getStatusgrid(grid,addDirection(elem, eachdirection)) == 'E':
						directionlist.append(eachdirection)
						#print(directionlist)
	#print("longeur", len(directions))
	for i in directions:# for each direction
		if directionlist.count(i) == 2 :# if there is two times the same direction -> sumito available
			moves.append([[m1,m2],i])
			pass	
	directionlist.clear()
	return None


if __name__=='__main__':
	def show(state):
		print('\n'.join([' '.join(line) for line in state['board']]))
		print()
	Game = Abalone
	state, next = Abalone(["jojo","jack"])

	#state['board'][6][2] = 'W'
	state['board'][4][1] = 'W'
	state['board'][3][4] = 'W'
	#state['board'][3][3] = 'W'
	state['board'][3][5] = 'B'
	state['board'][3][6] = 'B'
	#state['board'][6][2] = 'B'
	state['board'][3][7] = 'W'
	#state['board'][4][3] = 'B'

