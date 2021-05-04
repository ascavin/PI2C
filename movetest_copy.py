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


	
def boucleangleonemarble(li,ci,state):
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
	elif li == 8 and ci ==8:
		print("8 and 4")
		for elem in ["W","NW","NE"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)	

	elif li == 0 and ci ==0:
		print("0 and 0")
		for elem in ["SW","SE","E"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)		
		pass

	elif li == 8 and ci ==4:
		print("8 and 4")
		for elem in ["NW","NE","E"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)

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

def bouclestayonboard2marble(state,li,ci):
	Opponent = mvt.opponent(mvt.symbols[state['current']])
	Allie = mvt.symbols[state['current']]
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
		for elem in ["NW","NE","E"]:
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

	elif li == 0 and ci == 0:
		print("4 and 8")
		for elem in ["SW","SE","E"]:
			#print(mvt.addDirection((li,ci),elem))
			xi,yi=mvt.addDirection((li,ci),elem)
			if state['board'][xi][yi] == "E":
				isitp = True
				#result.append([mvt.addDirection((li,ci),elem),elem])
				dictio[elem] = (xi,yi)				

	elif li == 8 and ci == 8:
		print("8 and 8")
		for elem in ["W","NW","NE"]:
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
			xi,yi=mvt.addDirection((xi,yi),elem)
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

def boucle2marblesexceptionmove(dictio1,dictio2,pos1,pos2):# mouvements possible pour les 2 billes
	dict2marble = {}
	print(dictio1)
	print(dictio2)
	x1,y1 = pos1
	x2,y2 = pos2
	#print(pos2)
	statevar3 = False
	for elem in dictio1:		
		for otherelem in dictio2:
			
			if elem == otherelem: # si 2 deplacements en commun ( deplacement en parallele)
				#print("ok")
				dict2marble[elem] = dictio1[elem]
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

def moveennemi(state,pos,dictio,currentmarble):
	li,ci= pos
	opponentplayer = mvt.opponent(currentmarble)
	for elem in dictio:# pour chaque alignement
		elemopo = opposite[elem]
		# je veux regarder sur la ligne si il ny a pas dadversaire 
		xv,yv=mvt.addDirection((li,ci),elem)#coordonne du voisin 
		xvp1,yvp1 = mvt.addDirection((xv,yv),elem)#1 case apres le voisin
		xvp2,yvp2 = mvt.addDirection((xvp1,yvp1),elem)# 2 cases apres le voisin
		xim1,yim1 = mvt.addDirection((li,ci),elemopo)#1case avant moi direction oppose
		xim2,yim2 = mvt.addDirection((xim1,yim1),elemopo)#2 cases avant moi direction oppose
		#print("xv,yv",xv,yv,"xvp1,yvp1",xvp1,yvp1,"xvp2,yvp2",xvp2,yvp2,"xim1,yim1",xim1,yim1,"xim2,yim2",xim2,yim2)
		
		if state['board'][xvp1][yvp1] == opponentplayer and state['board'][xvp2][yvp2] == "E":
			dictio[elem][elem] = (xv,yv)
			#print("ok",dictio[elem])
			pass

		if state['board'][xim1][yim1] == opponentplayer and state['board'][xim2][yim2] == "E":
			dictio[elem][opposite[elem]] = (xim1,yim1)
			pass

	return False

def moveaMarbleispossible(state, pos):
	li, ci = pos
	return boucleangleonemarble(li,ci,state)

def move2Marbleispossible(state,pos):
	l1,c1 = pos#possition of the marble
	statevarneighbour = False
	dictio13 = {}
	Allie = mvt.symbols[state['current']]# get allie symbole
	if mvt.findNeighbor(state['board'],(l1,c1),Allie,True)[0] :# si il y a voisin
		for elem in list(mvt.findNeighbor(state['board'],(l1,c1),Allie,True)[1].keys()): # regarde pour chaque direction des voisins
			xn,yn = mvt.findNeighbor(state['board'],(l1,c1),Allie,True)[1][elem]		#recupere les coordonnes de chaque voisin

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
	moveennemi(state,pos,dictio13,Allie)

	return statevar3,dictio13

def canImoveamarblenexttoallie(state,pos):
	return False

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
	state['board'][4][4] = 'B'
	state['board'][4][5] = 'B'
	state['board'][4][6] = 'W'
	state['board'][4][3] = 'W'
	state['board'][4][7] = 'W'
	state['board'][4][2] = 'W'
	#state['board'][5][4] = 'B'
	show(state)
	#moveaMarbleispossible(state, (4,4))
	#print(moveaMarbleispossible(state, (4,3)))
	#print(mvt.findNeighbor(state['board'],(4,3),"W",True))	
	#print(mvt.findNeighbor(state['board'],(4,3),"W",True))
	print(move2Marbleispossible(state,(4,4)))
	#print(list(mvt.findNeighbor(state['board'],(4,4),'B',True)[1].keys()))
	#print(mvt.findNeighbor(state['board'],(4,4),'B',True)[1]['NW'])




#fct : is it possible to move marble allies ? (is there empty case around allies marble ? )return bool value
#mvt.getStatus()