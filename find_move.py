import move
import gamestest as game
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

def opponent(color):
	if color == 'W':
		return 'B'
	return 'W'

def addDirection(pos, direction):
	D = directions[direction]
	return (pos[0] + D[0], pos[1] + D[1])

def isOnBoard(pos):
	l, c = pos
	if min(pos) < 0:
		return False
	if max(pos) > 8:
		return False
	if abs(c-l) >= 5:
		return False
	return True

def getStatusgrid(state, pos):
	#if not isOnBoard(pos):
	#	raise game.BadMove('The position {} is outside the board'.format(pos))
	return state[pos[0]][pos[1]]

def findMove(grid,marble,symbol):
	moves=[]
	alignement=[]
	possibilities=[]
	for direction in directions :
		#print('test diretion :',direction)
		find=True
		e=1        #nombre d'élément de l'alignement
		alignement.clear()
		while find and e<5:           
			#print("neighbor",(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e),neighbor(grid,(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e)))
			#print(alignement.append(neighbor(grid,(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e))))
			alignement.append(neighbor(grid,(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e)))
			possibilities=getPossibilities(symbol)
			#print(alignement)
			for i,possibilitie in enumerate(possibilities):
					 
				#print("i",i) 
				# if i == 7:
				# 	print(possibilitie)   
				# 	print("-------------------------")

				#if direction =='W':			
				#print("possibilitie",possibilitie)
					#print("alignement",alignement) 
				if possibilitie == alignement :	
					#print(possibilitie)
					#print(alignement)	
					m1 = [marble[0],marble[1]]
					m2 = [marble[0]+directions[direction][0],marble[1]+directions[direction][1]]
					m3 = [marble[0]+directions[direction][0]*2,marble[1]+directions[direction][1]*2]
								
					find=False
										
					if i == 0: 
						print("0")
						moves.append([[m1],direction])
						
					if i == 1:
						print("1")
						pass
					if i == 2: 
						print("2")
						moves.append([[m1,m2],direction])
						sumito2m(m1,m2,moves,direction)
					if i==3:
						print("3")
						sumito2m(m1,m2,moves,direction)
						pass
					if i == 4:
						print("4")
						moves.append([[m1,m2,m3],direction])
						sumito3m(m1,m2,m3,moves,direction)
							
					if i == 5:
						print("5")
						sumito3m(m1,m2,m3,moves,direction)
						pass
					if (i == 6):
						moves.append([[m1,m2],direction])
						sumito2m(m1,m2,moves,direction)
						print("6")
					if i == 7:
						print("7")
						moves.append([[m1,m2],direction])
						sumito2m(m1,m2,moves,direction)	
								
					if i == 8:
						print("8")
						sumito2m(m1,m2,moves,direction)
						pass
					if i == 9:
						print("9")
						sumito3m(m1,m2,m3,moves,direction)
						pass
					if i == 10 or i==11:#possible sumito
						print("10 et 11")
						moves.append([[m1,m2,m3],direction])
						sumito3m(m1,m2,m3,moves,direction)
 
						print("ok")

					if i == 12 or i==13:
						print("12 et 13")
						moves.append([[m1,m2,m3],direction])
						sumito3m(m1,m2,m3,moves,direction)
						
					if i == 14:
						print("14")
						sumito3m(m1,m2,m3,moves,direction)
						pass


					break


			e=e+1   
	return moves

#manque les mouvements en paralleles

			
def neighbor(grid,marble):
	li,ci = marble
	#print(marble)
	if  (0<=li<=4 and 0<=ci<=4) or (5<=li<=8 and 5<=ci<=8) or (5<=li<=8 and 0<=ci<=4 and not grid[li][ci] == 'X') or (0<=li<=4 and 5<=ci<=8 and not grid[li][ci] == 'X'):
		res=grid[marble[0]][marble[1]]

		return res
	else : 
		return 'X'

def isonboard(grid,marble):
	if  (0<=li<=4 and 0<=ci<=4) or (5<=li<=8 and 5<=ci<=8) or (5<=li<=8 and 0<=ci<=4 and not grid[li][ci] == 'X') or (0<=li<=4 and 5<=ci<=8 and not grid[li][ci] == 'X'):
		return True
	else :
		return False 

def getPossibilities(symbol):         
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

					#['E'],                 			#:True		#0
					#['X'] or out 						#: False	#1
					#['B','E'],             			#:True		#2
					#['B','X'] or ['B',out] 			#: False	#3
					#['B','B','E'],         				#:True		#4
					#['B','B','X'] or ['B','B',out] 		#: False	#5
					#['B','W','E'],         				#:True		#6
					#['B','W','X'], or  ['B','W',out]   	#:True		#7
					#['B','W','W'],         				#:False		#8
					#['B','B','B'],         				#:False		#9
					#['B','B','W','E'],     					#:True		#10
					#['B','B','W','X'] or ['B','B','W',out]		#:True		#11
					#['B','B','W','W','E'], 						#:True		#12
					#['B','B','W','W','X'] or ['B','B','W','W',out]	#:True		#13
					#['B','B','W','W','W'], 						#:False		#14
	return possibilities

def sumito3m(m1,m2,m3,moves,direction):
	directionlist = []
	for elem in [m1,m2,m3]:#pour chaque position
		for eachdirection in directions :#pour chaque direction
			#print(direction)
			if eachdirection == direction or eachdirection == opposite[direction]:
				pass
			else:# directions de lalignement exclu
				if getStatusgrid(grid,addDirection(elem, eachdirection)) == 'E':
					directionlist.append(eachdirection)
					print(directionlist)
	for i in range(0,len(directions)-3):
		if directionlist.count(directionlist[i]) == 3 :
			moves.append([[m1,m2,m3],directionlist[i]])
			pass	
	directionlist.clear()
	return None

def sumito2m(m1,m2,moves,direction):
	directionlist = []
	for elem in [m1,m2]:#pour chaque position
		for eachdirection in directions :#pour chaque direction
			#print(direction)
			if eachdirection == direction or eachdirection == opposite[direction]:
				pass
			else:# directions de lalignement exclu
				if getStatusgrid(grid,addDirection(elem, eachdirection)) == 'E':
					directionlist.append(eachdirection)
					print(directionlist)
	for i in range(0,len(directions)-3):
		if directionlist.count(directionlist[i]) == 2 :
			moves.append([[m1,m2],directionlist[i]])
			pass	
	directionlist.clear()
	return None

if __name__=='__main__':  
	grid=[
			['W', 'W', 'W', 'W', 'W', 'W', 'X', 'X', 'X'],
			['W', 'W', 'W', 'W', 'W', 'W', 'X', 'X', 'X'],
			['E', 'E', 'W', 'W', 'W', 'E', 'E', 'X', 'X'],
			['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'X'],
			['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
			['X', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
			['X', 'X', 'E', 'E', 'B', 'B', 'B', 'E', 'E'],
			['X', 'X', 'X', 'B', 'B', 'B', 'B', 'B', 'B'],
			['X', 'X', 'X', 'X', 'B', 'B', 'B', 'B', 'B']
		]
	def show(state):
		print('\n'.join([' '.join(line) for line in state]))
		print()
	
	#grid[4][0] = 'W'
	grid[4][0] = 'B'
	grid[4][1] = 'B'
	grid[4][2] = 'B'
	grid[4][3] = 'B'
	#grid[4][3] = 'B'
	grid[5][3] = 'W'
	#grid[3][2] = 'W'
	#grid[3][1] = 'W'

	result=findMove(grid,(4,1),'B')
	show(grid)
	print(result)

			
	

