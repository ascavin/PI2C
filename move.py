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
		
def isOnBoard(pos):
	l, c = pos
	if min(pos) < 0:
		return False
	if max(pos) > 8:
		return False
	if abs(c-l) >= 5:
		return False
	return True

def isnotOnBoard(pos):
	l, c = pos
	if min(pos) < 0:
		return True
	if max(pos) > 8:
		return True
	if abs(c-l) >= 5:
		return True
	return False

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

def isnotEmpty(state, pos):
	return getStatus(state, pos) == 'W' or getStatus(state, pos) == 'B'

def isFree(state, pos):
	if isOnBoard(pos):
		return isEmpty(state, pos)
	else:
		return True

def isout(state, pos):
	if isnotOnBoard(pos) or getStatus(state, pos) == 'X':
		return True
	else:
		return False

def isboardFree(state, pos):
	if isOnBoard(pos):
		return isnotEmpty(state, pos)
	else:
		return False

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
		print("v1",isneigbour,dictneighbour)
		return isneigbour,dictneighbour
	return neighbors



def bouclecenter(li,ci):

		for x in [li-1,li,li+1]:
			for y in [ci-1,ci,ci+1]:# tout autour de la bille
				print(x,y)
				#status = getStatus(state, (x,y))
				#if status == 'E' :
				#	statevar = True
				#else : 
				#	statevar = False
		return False


	
def boucleangleonemarble(li,ci,state):
	#result = []
	dictio = {}
	isitp = False
	if li == 4 and ci == 0:
		print("4 and 0")
		for elem in ["NE","E","SE"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)

		pass
	elif li == 8 and ci ==8:
		print("8 and 4")
		for elem in ["W","NW","NE"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)	

	elif li == 0 and ci ==0:
		print("0 and 0")
		for elem in ["SW","SE","E"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)		
		pass

	elif li == 8 and ci ==4:
		print("8 and 4")
		for elem in ["NW","NE","E"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)

	elif li == 0 and ci == 4:
		print("0 and 4")
		for elem in ["W","SW","SE"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif li == 4 and ci == 8:
		print("4 and 8")
		for elem in ["NW","W","SW"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif 4<li<8 and 0<ci<4:
		print("48 and 04")
		for elem in ["NW","NE","E","SE"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif 4<li<8 and 4<ci<8:
		print("48 and 04")
		for elem in ["W","NW","NE","E"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass	
	elif 0<li<4 and 4<ci<8:
		print("04 and 48")
		for elem in ["NW","W","SW","SE"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif li==0 and 0<ci<4:
		print("0 and 04")
		for elem in ["W","SW","SE","E"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif 0<li<4 and ci==0:
		print("04 and 0")
		for elem in ["SW","SE","E","NE"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif 4<li<8 and ci==8:
		print("48 and 8")
		for elem in ["SW","W","NW","NE"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif li==8 and 4<ci<8:
		print("8 and 48")
		for elem in ["W","NW","NE","E"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	
	else : 
		#print("center")
		for elem in ["W","NW","NE","E","SE","SW"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)

		pass
	#result.insert(0,isitp)
	return isitp,dictio

def isnotOnBoard(pos):
	l, c = pos
	if min(pos) < 0:
		return True
	if max(pos) > 8:
		return True
	if abs(c-l) >= 5:
		return True
	return False

def bouclestayonboard2marble(state,li,ci):
	Opponent = opponent(symbols[state['current']])
	Allie = symbols[state['current']]
	#result = []
	dictio = {}
	isitp = False
	if li == 4 and ci == 0:
		#print("4 and 0")
		for elem in ["NE","E","SE"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)
			
		pass
	elif li == 8 and ci ==4:
		#print("8 and 4")
		for elem in ["NW","NE","E"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)
					
		pass
	elif li == 0 and ci == 4:
		#print("0 and 4")
		for elem in ["W","SW","SE"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
					
		pass
	elif li == 4 and ci == 8:
		#print("4 and 8")
		for elem in ["NW","W","SW"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)	

	elif li == 0 and ci == 0:
		#print("4 and 8")
		for elem in ["SW","SE","E"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)				

	elif li == 8 and ci == 8:
		#print("8 and 8")
		for elem in ["W","NW","NE"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)

		pass
	elif 4<li<8 and 0<ci<4:
		#print("48 and 04")
		for elem in ["NW","NE","E","SE"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)
					
		pass
	elif 4<li<8 and 4<ci<8:
		#print("48 and 04")
		for elem in ["W","NW","NE","E"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)	
				
		pass	
	elif 0<li<4 and 4<ci<8:
		#print("04 and 48")
		for elem in ["NW","W","SW","SE"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)
					
		pass
	elif li==0 and 0<ci<4:
		#print("0 and 04")
		for elem in ["W","SW","SE","E"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)	
				
		pass
	elif 0<li<4 and ci==0:
		#print("04 and 0")
		for elem in ["SW","SE","E","NE"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)	
				
		pass
	elif 4<li<8 and ci==8:
		#print("48 and 8")
		for elem in ["SW","W","NW","NE"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)	
				
		pass
	elif li==8 and 4<ci<8:
		#print("8 and 48")
		for elem in ["W","NW","NE","E"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)
		pass
	
	else : 
		#print("center")
		for elem in ["W","NW","NE","E","SE","SW"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)
			
		pass
	#result.insert(0,isitp)
	return isitp,dictio

def boucle2marblesexceptionmove(dictio1,dictio2,pos1,pos2):# mouvements possible pour les 2 billes
	dict2marble = {}
	dictio11 = dictio1
	dictio22 = dictio2
	#print(dictio1)
	#print(dictio2)
	x1,y1 = pos1
	x2,y2 = pos2
	#print("ok1")
	statevar3 = False

	for elem in dictio1:		
		for otherelem in dictio2:
			print("ok2")
			if elem == otherelem: # si 2 deplacements en commun ( deplacement en parallele)
				#print("ok")
				dict2marble[elem] = dictio1[elem]
				#print(dictio1[elem])
				statevar3 = True

	for otherelem in dictio2:
		# deplacements en serie 
		if (dictio2[otherelem][0],dictio2[otherelem][1]-2) == pos1 or (dictio2[otherelem][0],dictio2[otherelem][1]+2) == pos1 :#axe des y vu du voisin
			dict2marble[otherelem] = dictio2[otherelem]
			#print("other",elem,dictio2[otherelem],otherelem)
			pass
	
		elif (dictio2[otherelem][0]-2,dictio2[otherelem][1]) == pos1 or (dictio2[otherelem][0]+2,dictio2[otherelem][1]) == pos1 :#axe des x vu du voisin
			dict2marble[otherelem] = dictio2[otherelem]
			pass
		# en diagonale 
		elif (dictio2[otherelem][0]-2,dictio2[otherelem][1]-2) == pos1 or (dictio2[otherelem][0]+2,dictio2[otherelem][1]+2) == pos1 :#diag vu du voisin
			dict2marble[otherelem] = dictio2[otherelem]
			#print("other",elem,dictio2[otherelem],otherelem)
			pass		

	for elem in dictio1:		
		if (dictio1[elem][0],dictio1[elem][1]+2) == pos2 or (dictio1[elem][0],dictio1[elem][1]-2) == pos2 : # axe des y vue de moi
			dict2marble[elem] = dictio1[elem]
			#print("ok")
			#print("me",elem,dictio1[elem])
			pass
		
		elif (dictio1[elem][0]+2,dictio1[elem][1]) == pos2 or (dictio1[elem][0]-2,dictio1[elem][1]) == pos2 :# axes des x vu de moi
			dict2marble[elem] = dictio1[elem]
			pass

		elif (dictio1[elem][0]+2,dictio1[elem][1]+2) == pos2 or (dictio1[elem][0]-2,dictio1[elem][1]-2) == pos2 : #diag vue de moi
			dict2marble[elem] = dictio1[elem]
			#print("me",elem,dictio1[elem])
			pass

	print(dict2marble)		
	return statevar3,dict2marble

def moveennemi2m(state,pos,dictio,currentmarble):
	li,ci= pos
	opponentplayer = opponent(currentmarble)
	for elem in dictio:# pour chaque alignement
		elemopo = opposite[elem]
		# je veux regarder sur la ligne si il ny a pas dadversaire 
		xv,yv=addDirection((li,ci),elem)#coordonne du voisin 

		#print(isboardFree(state, addDirection((xv,yv),elem)),addDirection((xv,yv),elem),xv,yv,elem)
		#if isboardFree(state, addDirection((xv,yv),elem)):
		if isOnBoard(addDirection((xv,yv),elem)):
			#print("ok")
			xvp1,yvp1 = addDirection((xv,yv),elem)#1 case apres le voisin
			
			#print(isout(state,addDirection((xvp1,yvp1),elem)))
			if isFree(state, addDirection((xvp1,yvp1),elem)) or isout(state,addDirection((xvp1,yvp1),elem)):
			#if isOnBoard(addDirection((xvp1,yvp1),elem)):
				#print("ok2")
				
				xvp2,yvp2 = addDirection((xvp1,yvp1),elem)# 2 cases apres le voisin
				
				if state['board'][xvp1][yvp1] == opponentplayer and (state['board'][xvp2][yvp2] == "E" or state['board'][xvp2][yvp2] == "X") :
					dictio[elem][elem] = (xv,yv)
					#print("ok",dictio[elem])
					pass



		#if isFree(state, addDirection((xvp2,yvp2),elemopo)):
		if isOnBoard(addDirection((li,ci),elemopo)):
			#print("ok")		
			xim1,yim1 = addDirection((li,ci),elemopo)#1case avant moi direction oppose

			#print(isout(state,addDirection((xim1,yim1),elemopo)))
			if isFree(state, addDirection((xim1,yim1),elemopo)) or isout(state, addDirection((xim1,yim1),elemopo)):
			#if isOnBoard(addDirection((xim1,yim1),elemopo)):
				xim2,yim2 = addDirection((xim1,yim1),elemopo)#2 cases avant moi direction oppose
				#print("xv,yv",xv,yv,"xvp1,yvp1",xvp1,yvp1,"xvp2,yvp2",xvp2,yvp2,"xim1,yim1",xim1,yim1,"xim2,yim2",xim2,yim2)
				#print("ok")

				if state['board'][xim1][yim1] == opponentplayer and (state['board'][xim2][yim2] == "E" or state['board'][xim2][yim2] == "X"):
					dictio[elem][opposite[elem]] = (xim1,yim1)
					#print("ok")		
					pass

	return False

def moveaMarbleispossible(state, pos):
	li, ci = pos
	return boucleangleonemarble(li,ci,state)

def move3Marbleispossible(state,pos):
	l1,c1 = pos
	statevarneighbour = False
	dictiofinal = {}
	Allie = symbols[state['current']]# get allie symbole
	print(find2Neighbor(state['board'],pos,Allie,True))
	if find2Neighbor(state['board'],(l1,c1),Allie,True)[0] :# si il y a voisin
		for elem in list(find2Neighbor(state['board'],(l1,c1),Allie,True)[1].keys()): # regarde pour chaque direction des voisins
			xn,yn = find2Neighbor(state['board'],(l1,c1),Allie,True)[1][elem][0]		#recupere les coordonnes du voisin 1
			xnp1,ynp1 = find2Neighbor(state['board'],(l1,c1),Allie,True)[1][elem][1] #recupere les coordonnes du voisin 1
			#print(find2Neighbor(state['board'],(l1,c1),Allie,True)[1][elem][0])
			print(xn,yn,xnp1,ynp1)

	return None

def move2Marbleispossible(state,pos):
	l1,c1 = pos#possition of the marble
	statevarneighbour = False
	dictio13 = {}
	Allie = symbols[state['current']]# get allie symbole
	if findNeighborv2(state['board'],(l1,c1),Allie,True)[0] :# si il y a voisin
		for elem in list(findNeighborv2(state['board'],(l1,c1),Allie,True)[1].keys()): # regarde pour chaque direction des voisins
			xn,yn = findNeighborv2(state['board'],(l1,c1),Allie,True)[1][elem]		#recupere les coordonnes de chaque voisin

			statevar1,dictio1 = bouclestayonboard2marble(state,l1,c1)# mouvement possible pour ma bille 
			statevar2,dictio2 = bouclestayonboard2marble(state,xn,yn)# mouvement possible pour mon voisin allie
			#print(dictio1)
			#print(dictio2)
			pos1 = l1,c1
			pos2 = xn,yn
			#print("ok")
			statevar3,dictio12 = boucle2marblesexceptionmove(dictio1,dictio2,pos1,pos2)# mouvements possible pour les 2 billes
			dictio13[elem] = dictio12
		pass
	else :
		return statevarneighbour 
	moveennemi2m(state,pos,dictio13,Allie)
	posmarbles = findNeighborv2(state['board'],(l1,c1),Allie,True)
	posmarbles[1]["marble1"] = pos
	#dictio13["marbles"] = pos2marbles(state, pos,Allie)# recupere les cordonne de la bille initiale et des voisins
	return statevar3,posmarbles[1],dictio13
#############################################################
############################################################
#def pos2marbles(state,pos,Allie):
#	l1,c1 = pos#position of the marble
#	dictioposmarbles = {}
#	dictioposmarbles["marble1"] = pos
#	if findNeighborv2(state['board'],(l1,c1),Allie,True)[0] :# si il y a voisin
#		for elem in list(findNeighborv2(state['board'],(l1,c1),Allie,True)[1].keys()): # regarde pour chaque direction des voisins
#			xn,yn = findNeighborv2(state['board'],(l1,c1),Allie,True)[1][elem]		#recupere les coordonnes de chaque voisin
#			print(elem)
#			dictioposmarbles[elem] = (xn,yn)
#	#print(dictioposmarbles)
#	return dictioposmarbles
#################################################################
#################################################################
def canImoveamarblenexttoallie(state,pos):
	return False

def findNeighborv2(grid,location,symbol,varstate=False):
	isneigbour = False
	dictneighbour = {}
	for direction in list(directions.keys()):
		if isOnBoard(addDirection(location,direction)):
			dictneighbour[direction] = addDirection(location,direction)
			isneigbour = True
	#print("v2",isneigbour,dictneighbour)
	return isneigbour,dictneighbour 

def find2Neighbor(grid,location,symbol,varstate=False):
	neighbors=[]
	isneigbour = False
	dictneighbour = {}
	if (location[1]<=7) :
		if (grid[location[0]][location[1]+1]==symbol) and (grid[location[0]][location[1]+2]==symbol):  #E
			neighbors.append((location[0],location[1]+1,'E'))
			neighbors.append((location[0],location[1]+2,'E'))
			dictneighbour["E"] = ((location[0],location[1]+1),(location[0],location[1]+2))
			isneigbour = True
	if (location[1]>=1):
		if (grid[location[0]][location[1]-1]==symbol) and (grid[location[0]][location[1]-2]==symbol):  #W
			neighbors.append((location[0],location[1]-1,'W'))
			neighbors.append((location[0],location[1]-2,'W'))
			dictneighbour["W"] = ((location[0],location[1]-1),(location[0],location[1]-2))
			isneigbour = True
	if (location[1]<=7 and location[0]<=7):
		if (grid[location[0]+1][location[1]+1]==symbol) and (grid[location[0]+2][location[1]+2]==symbol):  #SE
			neighbors.append((location[0]+1,location[1]+1,'SE'))
			neighbors.append((location[0]+2,location[1]+2,'SE'))
			dictneighbour["SE"] = ((location[0]+1,location[1]+1),(location[0]+2,location[1]+2))
			isneigbour = True
	if  (location[1]>=1 and location[0]>=1):
		if (grid[location[0]-1][location[1]-1]==symbol) and (grid[location[0]-2][location[1]-2]==symbol):  #NW
			neighbors.append((location[0]-1,location[1]-1,'NW'))
			neighbors.append((location[0]-2,location[1]-2,'NW'))
			dictneighbour["NW"] = ((location[0]-1,location[1]-1),(location[0]-2,location[1]-2))
			isneigbour = True
	if (location[0]>=1):
		if (grid[location[0]-1][location[1]]==symbol) and (grid[location[0]-2][location[1]]==symbol):  #NE
			neighbors.append((location[0]-1,location[1],'NE'))
			neighbors.append((location[0]-2,location[1],'NE'))
			dictneighbour["NE"] = ((location[0]-1,location[1]),(location[0]-2,location[1]))
			isneigbour = True
	if (location[0]<=7) :
		if (grid[location[0]+1][location[1]]==symbol) and (grid[location[0]+2][location[1]]==symbol):  #SW
			neighbors.append((location[0]+1,location[1],'SW'))
			neighbors.append((location[0]+2,location[1],'SW'))
			dictneighbour["SW"] = ((location[0]+1,location[1]),(location[0]+2,location[1]))
			isneigbour = True

	if varstate == True :
		print("v1",isneigbour,dictneighbour)
		return isneigbour,dictneighbour
	return neighbors





if __name__=='__main__':
	def show(state):
		print('\n'.join([' '.join(line) for line in state['board']]))
		print()
	Game = Abalone
	state, next = Abalone(["jojo","jack"])
	#print(state)
	#state['board'][4][3] = 'B'
	#state['board'][4][4] = 'B'
		#state['board'][4][1] = 'W'
		#state['board'][3][1] = 'W'
	#state['board'][3][3] = 'W'
		#state['board'][5][2] = 'B'
		#state['board'][4][2] = 'B'
	#state['board'][6][2] = 'B'
		#state['board'][6][2] = 'W'
	#state['board'][4][3] = 'B'
	#state['board'][4][4] = 'B'
		#state['board'][5][1] = 'W'
	#state['board'][3][1] = 'W'
	#state['board'][3][3] = 'W'
		#state['board'][5][2] = 'B'
		#state['board'][5][3] = 'B'
	#state['board'][6][2] = 'B'
	#state['board'][6][2] = 'W'
	state['board'][4][1] = 'W'
	state['board'][3][4] = 'W'
	#state['board'][3][3] = 'W'
	state['board'][3][5] = 'B'
	state['board'][3][6] = 'B'
	#state['board'][6][2] = 'B'
	state['board'][3][7] = 'W'
	#state['board'][4][3] = 'B'

	show(state)
	#moveaMarbleispossible(state, (4,4))

	#print(moveaMarbleispossible(state, (4,3)))
	print(move2Marbleispossible(state,(0,0)))
	#print(move3Marbleispossible(state,(5,5)))
	#print(findNeighbor(state['board'],(8,8),'B',True))
	#print(addDirection((0,0),'NW'))



#fct : is it possible to move marble allies ? (is there empty case around allies marble ? )return bool value
#getStatus()