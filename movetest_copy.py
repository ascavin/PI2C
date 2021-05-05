import gamestest as game
import movetest as mvt
symbols = ['B', 'W']

directions = {
	'NE': (-1,  0),
	'SW': ( 1,  0),
	'NW': (-1, -1),
	'SE': ( 1,  1),
	 'E': ( 0,  1),
	 'W': ( 0, -1)
}

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
		return isneigbour,dictneighbour
	return neighbors

def opponent(color):
	if color == 'W':
		return 'B'
	return 'W'

def addDirection(pos, direction):
	D = directions[direction]
	return (pos[0] + D[0], pos[1] + D[1])

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
		print("4 and 0")
		for elem in ["NE","E","SE"]:
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
					
		pass
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

	elif li == 0 and ci == 0:
		print("4 and 8")
		for elem in ["SW","SE","E"]:
			#print(addDirection((li,ci),elem))
			xi,yi=addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)				

	elif li == 8 and ci == 8:
		print("8 and 8")
		for elem in ["W","NW","NE"]:
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
			xi,yi=addDirection((xi,yi),elem)
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
	#print(dictio1)
	#print(dictio2)
	x1,y1 = pos1
	x2,y2 = pos2
	#print(pos2)
	statevar3 = False
	for elem in dictio1:		
		for otherelem in dictio2:
			
			if elem == otherelem: # si 2 deplacements en commun ( deplacement en parallele)
				#print("ok")
				dict2marble[elem] = dictio1[elem]
				#print(dictio1[elem])
				statevar3 = True

			# deplacements en serie 
			elif (dictio2[otherelem][0],dictio2[otherelem][1]-2) == pos1 or (dictio2[otherelem][0],dictio2[otherelem][1]+2) == pos1 :#axe des y vu du voisin
				dict2marble[otherelem] = dictio2[otherelem]
				#print("other",elem,dictio2[otherelem],otherelem)
				
				pass

			elif (dictio2[otherelem][0]-2,dictio2[otherelem][1]) == pos1 or (dictio2[otherelem][0]+2,dictio2[otherelem][1]) == pos1 :#axe des x vu du voisin
				dict2marble[otherelem] = dictio2[otherelem]
				
				pass
			elif (dictio1[elem][0],dictio1[elem][1]+2) == pos2 or (dictio1[elem][0],dictio1[elem][1]-2) == pos2 : # axe des y vue de moi
				dict2marble[elem] = dictio1[elem]
				#print("ok")
				#print("me",elem,dictio1[elem])
				pass
			elif (dictio1[elem][0]+2,dictio1[elem][1]) == pos2 or (dictio1[elem][0]-2,dictio1[elem][1]) == pos2 :# axes des x vu de moi
				dict2marble[elem] = dictio1[elem]
				pass

			# en diagonale 
			elif (dictio2[otherelem][0]-2,dictio2[otherelem][1]-2) == pos1 or (dictio2[otherelem][0]+2,dictio2[otherelem][1]+2) == pos1 :#diag vu du voisin
				dict2marble[otherelem] = dictio2[otherelem]
				#print("other",elem,dictio2[otherelem],otherelem)
				pass
			elif (dictio1[elem][0]+2,dictio1[elem][1]+2) == pos2 or (dictio1[elem][0]-2,dictio1[elem][1]-2) == pos2 : #diag vue de moi
				dict2marble[elem] = dictio1[elem]
				#print("me",elem,dictio1[elem])
				pass	

	return statevar3,dict2marble

def moveennemi2m(state,pos,dictio,currentmarble):
	li,ci= pos
	opponentplayer = opponent(currentmarble)
	for elem in dictio:# pour chaque alignement
		elemopo = opposite[elem]
		# je veux regarder sur la ligne si il ny a pas dadversaire 
		xv,yv=addDirection((li,ci),elem)#coordonne du voisin 
		xvp1,yvp1 = addDirection((xv,yv),elem)#1 case apres le voisin
		xvp2,yvp2 = addDirection((xvp1,yvp1),elem)# 2 cases apres le voisin
		xim1,yim1 = addDirection((li,ci),elemopo)#1case avant moi direction oppose
		xim2,yim2 = addDirection((xim1,yim1),elemopo)#2 cases avant moi direction oppose
		#print("xv,yv",xv,yv,"xvp1,yvp1",xvp1,yvp1,"xvp2,yvp2",xvp2,yvp2,"xim1,yim1",xim1,yim1,"xim2,yim2",xim2,yim2)
		
		if state['board'][xvp1][yvp1] == opponentplayer and (state['board'][xvp2][yvp2] == "E" or state['board'][xvp2][yvp2] == "X") :
			dictio[elem][elem] = (xv,yv)
			#print("ok",dictio[elem])
			
			pass

		if state['board'][xim1][yim1] == opponentplayer and (state['board'][xim2][yim2] == "E" or state['board'][xvp2][yvp2] == "X"):
			dictio[elem][opposite[elem]] = (xim1,yim1)
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
	if findNeighbor(state['board'],(l1,c1),Allie,True)[0] :# si il y a voisin
		for elem in list(findNeighbor(state['board'],(l1,c1),Allie,True)[1].keys()): # regarde pour chaque direction des voisins
			xn,yn = findNeighbor(state['board'],(l1,c1),Allie,True)[1][elem]		#recupere les coordonnes de chaque voisin

			statevar1,dictio1 = bouclestayonboard2marble(state,l1,c1)# mouvement possible pour ma bille 
			statevar2,dictio2 = bouclestayonboard2marble(state,xn,yn)# mouvement possible pour mon voisin allie
			#print(dictio1)
			#print(dictio2)
			pos1 = l1,c1
			pos2 = xn,yn
			#print(pos2)
			statevar3,dictio12 = boucle2marblesexceptionmove(dictio1,dictio2,pos1,pos2)# mouvements possible pour les 2 billes
			dictio13[elem] = dictio12
		pass
	else :
		return statevarneighbour 
	moveennemi2m(state,pos,dictio13,Allie)
	posmarbles = findNeighbor(state['board'],(l1,c1),Allie,True)
	posmarbles[1]["marble1"] = pos
	#dictio13["marbles"] = pos2marbles(state, pos,Allie)# recupere les cordonne de la bille initiale et des voisins
	return statevar3,posmarbles[1],dictio13
#############################################################
############################################################
def pos2marbles(state,pos,Allie):
	l1,c1 = pos#position of the marble
	dictioposmarbles = {}
	dictioposmarbles["marble1"] = pos
	if findNeighbor(state['board'],(l1,c1),Allie,True)[0] :# si il y a voisin
		for elem in list(findNeighbor(state['board'],(l1,c1),Allie,True)[1].keys()): # regarde pour chaque direction des voisins
			xn,yn = findNeighbor(state['board'],(l1,c1),Allie,True)[1][elem]		#recupere les coordonnes de chaque voisin
			print(elem)
			dictioposmarbles[elem] = (xn,yn)
	#print(dictioposmarbles)
	return dictioposmarbles
#################################################################
#################################################################
def canImoveamarblenexttoallie(state,pos):
	return False

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
		return isneigbour,dictneighbour
	return neighbors



opposite = {
	'NE': 'SW',
	'SW': 'NE',
	'NW': 'SE',
	'SE': 'NW',
	'E': 'W',
	'W': 'E'
}

if __name__=='__main__':
	def show(state):
		print('\n'.join([' '.join(line) for line in state['board']]))
		print()
	state, next = mvt.Abalone(["jojo","jack"])
	#print(state)
	#state['board'][4][3] = 'B'
	#state['board'][4][4] = 'B'
	state['board'][4][5] = 'B'
	#state['board'][3][3] = 'W'
	state['board'][4][2] = 'W'
	state['board'][4][3] = 'W'
	#state['board'][5][2] = 'W'
	state['board'][4][4] = 'B'
	#state['board'][5][3] = 'B'
	#state['board'][5][6] = 'B'
	#state['board'][5][7] = 'B'
	#state['board'][6][6] = 'B'
	#state['board'][7][7] = 'B'
	#state['board'][4][4] = 'B'
	#state['board'][3][3] = 'B'
	show(state)
	#moveaMarbleispossible(state, (4,4))

	#print(moveaMarbleispossible(state, (4,3)))
	print(move2Marbleispossible(state,(4,4)))
	#print(move3Marbleispossible(state,(5,5)))



#fct : is it possible to move marble allies ? (is there empty case around allies marble ? )return bool value
#getStatus()