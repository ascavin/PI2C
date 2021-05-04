import gamestest as game
import movetest as mvt

def move(state, player):
	ask = isPossibleTo()
	if (isContact()) :#contact with opponent
		if (ask.moveOpponentMarbleOutOfTheBoard()):
			if (manyContact()):
				moves=computeMovesKeepingMaxNeighbour()# Compute wich valid move will keep the most neighbour and move out opponnent marble with maximum marbles to do it

				validMoves=ValidMove(Moves)               # return valid possibilites
				outMove=chooseMove(validMove)
			else :
				move=computeMoveWithMaxMarble()
				outmove=ValidMoves(move)    
		else : #If (!no possible to move opponnent marble out of the board) :
			if (manyContact()):
				if loseaMarbleofMyself():
					if MyMarblecanEscape():#Available position & no neighbour will out me
					  gotoNeighbourMarble()#close as possible
					else :
						#marble is lost 
						pass
				else :
					if AllMyMarbleareNeighbour():
						if (ask.moveOpponentMarbleCloseToTheBorder()):
							#move it 
							movemarble(position,numbersofmarble=max,direction=tochoose)
					
						else :
							if ask.moveaMarbleNexttoAllie():
								#move it 
								movemarble(position,numbersofmarble=max,direction=tochoose)
							else :
								if ask.moveaMarble():
									movemarble(position,numbersofmarble=max,direction=tochoose)
								else :
									pass
				
					else:
						if ask.moveaMarbleNexttoAllie():
							#move it 
							movemarble(position,numbersofmarble=max,direction=tochoose)
					
						else :
							marbleonborder = selectmarbleclosetotheborder()
							if marbleonborder == freetomove:
								#move it to the center 
								movemarble(position,numbersofmarble,direction=center)
							else :
								if othermarbleavailable():
									selectOtherMarble()
									#moveit
									movemarble(position,numbersofmarble,direction)
								else :
									pass
			else :
				if AllMyMarbleareNeighbour():
					if (ask.moveOpponentMarbleCloseToTheBorder()):
						#move it 
						movemarble(position,numbersofmarble=max,direction=tochoose)
					
					else :
						if ask.moveaMarbleNexttoAllie():
							#move it 
							movemarble(position,numbersofmarble=max,direction=tochoose)
						else :
							if ask.moveaMarble():
								movemarble(position,numbersofmarble=max,direction=tochoose)
							else :
								pass
				else:
					if ask.moveaMarbleNexttoAllie():
						#move it 
						movemarble(position,numbersofmarble=max,direction=tochoose)
					
					else :
						marbleonborder = selectmarbleclosetotheborder()
						if marbleonborder == freetomove:
							#move it to the center 
							movemarble(position,numbersofmarble,direction=center)
						else :
							if othermarbleavailable():
								selectOtherMarble()
								#moveit
								movemarble(position,numbersofmarble,direction)
							else :
								pass
						
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

directions = {
	'NE': (-1,  0),
	'SW': ( 1,  0),
	'NW': (-1, -1),
	'SE': ( 1,  1),
	 'E': ( 0,  1),
	 'W': ( 0, -1)
}                


def bouclecenter(li,ci):

		for x in [li-1,li,li+1]:
			for y in [ci-1,ci,ci+1]:# tout autour de la bille
				print(x,y)
				#status = mvt.getStatus(state, (x,y))
				#if status == 'E' :
				#	statevar = True
				#else : 
				#	statevar = False
		return False


	
def boucleangleonemarble(li,ci):
	#result = []
	dictio = {}
	isitp = False
	if li == 4 and ci == 0:
		print("4 and 0")
		for elem in ["NE","E","SE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)

		pass
	elif li == 8 and ci ==4:
		print("8 and 4")
		for elem in ["W","NW","NE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif li == 0 and ci == 4:
		print("0 and 4")
		for elem in ["W","SW","SE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif li == 4 and ci == 8:
		print("4 and 8")
		for elem in ["NW","W","SW"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif 4<li<8 and 0<ci<4:
		print("48 and 04")
		for elem in ["NW","NE","E","SE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif 4<li<8 and 4<ci<8:
		print("48 and 04")
		for elem in ["W","NW","NE","E"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass	
	elif 0<li<4 and 4<ci<8:
		print("04 and 48")
		for elem in ["NW","W","SW","SE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif li==0 and 0<ci<4:
		print("0 and 04")
		for elem in ["W","SW","SE","E"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif 0<li<4 and ci==0:
		print("04 and 0")
		for elem in ["SW","SE","E","NE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif 4<li<8 and ci==8:
		print("48 and 8")
		for elem in ["SW","W","NW","NE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	elif li==8 and 4<ci<8:
		print("8 and 48")
		for elem in ["W","NW","NE","E"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
		pass
	
	else : 
		#print("center")
		for elem in ["W","NW","NE","E","SE","SW"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
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

def boucleangle2marble(state,li,ci):
	Opponent = mvt.opponent(mvt.symbols[state['current']])
	Allie = mvt.symbols[state['current']]
	#print(Allie)
	#result = []
	dictio = {}
	isitp = False
	if li == 4 and ci == 0:
		print("4 and 0")
		for elem in ["NE","E","SE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)
			elif state['board'][xi][yi] == Opponent:# si il y a un adversaire
				xo,yo = mvt.addDirection((xi,yi),elem)
				if state['board'][xo][yo] =="E" or state['board'][xo][yo] =="X" or  isnotOnBoard((xo,yo)):# si il n'y a rien derriere 
					dictio[elem] = (xi,yi)
					isitp = True
					pass

		pass
	elif li == 8 and ci ==4:
		print("8 and 4")
		for elem in ["W","NW","NE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)
			elif state['board'][xi][yi] == Opponent:# si il y a un adversaire
				xo,yo = mvt.addDirection((xi,yi),elem)
				if state['board'][xo][yo] =="E" or state['board'][xo][yo] =="X" or  isnotOnBoard((xo,yo)):# si il n'y a rien derriere 
					dictio[elem] = (xi,yi)
					isitp = True
					pass			
		pass
	elif li == 0 and ci == 4:
		print("0 and 4")
		for elem in ["W","SW","SE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)			
			elif state['board'][xi][yi] == Opponent:# si il y a un adversaire
				xo,yo = mvt.addDirection((xi,yi),elem)
				if state['board'][xo][yo] =="E" or state['board'][xo][yo] =="X" or  isnotOnBoard((xo,yo)):# si il n'y a rien derriere 
					dictio[elem] = (xi,yi)
					isitp = True
					pass
		
		pass
	elif li == 4 and ci == 8:
		print("4 and 8")
		for elem in ["NW","W","SW"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)	
			elif state['board'][xi][yi] == Opponent:# si il y a un adversaire
				xo,yo = mvt.addDirection((xi,yi),elem)
				if state['board'][xo][yo] =="E" or state['board'][xo][yo] =="X" or  isnotOnBoard((xo,yo)):# si il n'y a rien derriere 
					dictio[elem] = (xi,yi)
					isitp = True
					pass					
		pass
	elif 4<li<8 and 0<ci<4:
		print("48 and 04")
		for elem in ["NW","NE","E","SE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)
			elif state['board'][xi][yi] == Opponent:# si il y a un adversaire
				xo,yo = mvt.addDirection((xi,yi),elem)
				if state['board'][xo][yo] =="E" or state['board'][xo][yo] =="X" or  isnotOnBoard((xo,yo)):# si il n'y a rien derriere 
					dictio[elem] = (xi,yi)
					isitp = True
					pass			
		pass
	elif 4<li<8 and 4<ci<8:
		print("48 and 04")
		for elem in ["W","NW","NE","E"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)	
			elif state['board'][xi][yi] == Opponent:# si il y a un adversaire
				xo,yo = mvt.addDirection((xi,yi),elem)
				if state['board'][xo][yo] =="E" or state['board'][xo][yo] =="X" or  isnotOnBoard((xo,yo)):# si il n'y a rien derriere 
					dictio[elem] = (xi,yi)
					isitp = True
					pass		
		pass	
	elif 0<li<4 and 4<ci<8:
		print("04 and 48")
		for elem in ["NW","W","SW","SE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)
			elif state['board'][xi][yi] == Opponent:# si il y a un adversaire
				xo,yo = mvt.addDirection((xi,yi),elem)
				if state['board'][xo][yo] =="E" or state['board'][xo][yo] =="X" or  isnotOnBoard((xo,yo)):# si il n'y a rien derriere 
					dictio[elem] = (xi,yi)
					isitp = True
					pass			
		pass
	elif li==0 and 0<ci<4:
		print("0 and 04")
		for elem in ["W","SW","SE","E"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)	
			elif state['board'][xi][yi] == Opponent:# si il y a un adversaire
				xo,yo = mvt.addDirection((xi,yi),elem)
				if state['board'][xo][yo] =="E" or state['board'][xo][yo] =="X" or  isnotOnBoard((xo,yo)):# si il n'y a rien derriere 
					dictio[elem] = (xi,yi)
					isitp = True
					pass		
		pass
	elif 0<li<4 and ci==0:
		print("04 and 0")
		for elem in ["SW","SE","E","NE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)	
			elif state['board'][xi][yi] == Opponent:# si il y a un adversaire
				xo,yo = mvt.addDirection((xi,yi),elem)
				if state['board'][xo][yo] =="E" or state['board'][xo][yo] =="X" or  isnotOnBoard((xo,yo)):# si il n'y a rien derriere 
					dictio[elem] = (xi,yi)
					isitp = True
					pass		
		pass
	elif 4<li<8 and ci==8:
		print("48 and 8")
		for elem in ["SW","W","NW","NE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)	
			elif state['board'][xi][yi] == Opponent:# si il y a un adversaire
				xo,yo = mvt.addDirection((xi,yi),elem)
				if state['board'][xo][yo] =="E" or state['board'][xo][yo] =="X" or  isnotOnBoard((xo,yo)):# si il n'y a rien derriere 
					dictio[elem] = (xi,yi)
					isitp = True
					pass		
		pass
	elif li==8 and 4<ci<8:
		print("8 and 48")
		for elem in ["W","NW","NE","E"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((xi,yi),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)
			elif state['board'][xi][yi] == Opponent:# si il y a un adversaire
				xo,yo = mvt.addDirection((xi,yi),elem)
				if state['board'][xo][yo] =="E" or state['board'][xo][yo] =="X" or  isnotOnBoard((xo,yo)):# si il n'y a rien derriere 
					dictio[elem] = (xi,yi)
					isitp = True
					pass
		pass
	
	else : 
		#print("center")
		for elem in ["W","NW","NE","E","SE","SW"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)
			elif state['board'][xi][yi] == Opponent:# si il y a un adversaire
				xo,yo = mvt.addDirection((xi,yi),elem)
				if state['board'][xo][yo] =="E" or state['board'][xo][yo] =="X" or  isnotOnBoard((xo,yo)):# si il n'y a rien derriere 
					dictio[elem] = (xi,yi)
					isitp = True
					pass

		pass
	#result.insert(0,isitp)
	return isitp,dictio

def boucle2marbles(dictio1,dictio2):
	dict2marble = {}
	#print(dictio1)
	#print(dictio2)
	statevar3 = False
	for elem in dictio1:		
		for otherelem in dictio2:
			#print(dictio1[elem])
			#print(dictio2[otherelem])
			if elem == otherelem:
				#print("ok")
				dict2marble[elem] = dictio1[elem]
				statevar3 = True
	return statevar3,dict2marble

def moveaMarbleispossible(state, pos):
	li, ci = pos
	return boucleangleonemarble(li, ci)

def move2Marbleispossible(state,pos1,pos2):
	l1,c1 = pos1
	l2,c2 = pos2
	statevar1,dictio1 = boucleangle2marble(state,l1, c1)
	statevar2,dictio2 = boucleangle2marble(state,l2, c2)
	statevar3,dictio12 = boucle2marbles(dictio1,dictio2)

	return statevar3,dictio12

def canImoveamarblenexttoallie(state,pos):
	return False


if __name__=='__main__':
	def show(state):
		print('\n'.join([' '.join(line) for line in state['board']]))
		print()
	state, next = mvt.Abalone(["jojo","jack"])
	#print(state)
	state['board'][4][3] = 'B'
	state['board'][4][4] = 'B'
	#state['board'][4][5] = 'W'
	#state['board'][4][6] = 'W'
	show(state)
	#moveaMarbleispossible(state, (4,4))
	#print(moveaMarbleispossible(state, (1,4)))
	print(move2Marbleispossible(state,(4,3),(4,4)))




#fct : is it possible to move marble allies ? (is there empty case around allies marble ? )return bool value
#mvt.getStatus()
