import move
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

def findMove(grid,marble,symbol):
	moves=[]
	alignement=[]
	possibilities=[]
	for direction in directions :
		#print('test diretion :',direction)
		find=True
		e=1        #nombre d'élément de l'alignement
		while find and e<5:           
			#print("neighbor",(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e))
			alignement.append(neighbor(grid,(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e)))
			possibilities=getPossibilities(symbol)
			for i,possibilitie in enumerate(possibilities):
				#print(alignement)
				#print("-------------------------")      
				if possibilitie == alignement :
					#print("possibilitie",possibilitie)
					#print("alignement",alignement)
					alignement.clear()
					find=False
					if i == 0: 
						moves.append([[[marble[0],marble[1]]],direction])
					if i == 1: 
						moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]]],direction])
					if i == 2:
						moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]],[marble[0]+directions[direction][0]*2,marble[1]+directions[direction][1]*2]],direction])
					if i == 3:
						moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]]],direction])
					if i == 4:
						pass
					if i == 5:
						pass
					if i == 6:
						moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]],[marble[0]+directions[direction][0]*2,marble[1]+directions[direction][1]*2]],direction])
					if i == 7:
						moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]],[marble[0]+directions[direction][0]*2,marble[1]+directions[direction][1]*2]],direction])
					break
			e=e+1   
	return moves

#Définir les goodmoves dans le plateau
#opti les possibilities
#définie les limites du plateau
#faire une fonction qui calcule les position à un rang n

			
def neighbor(grid,marble):
	li,ci = marble

	print(marble)
	if  (0<=li<=4 and 0<=ci<=4) or (5<=li<=8 and 5<=ci<=8) or (5<=li<=8 and 0<=ci<=4 and not grid[li][ci] == 'X') or (0<=li<=4 and 5<=ci<=8 and not grid[li][ci] == 'X'):
		res=grid[marble[0]][marble[1]]
		return res
	else : 
		return 'X'

def getPossibilities(symbol):         
	possibilities =[
					['E'],                 #:True,    #0    #je sors une de mes billes si W en bordure ou E à l'exterieur du plateau
					[symbol,'E'],             #:True,    #1    #je sors une de mes billes si W en bordure ou E à l'exterieur du plateau
					[symbol,symbol,'E'],         #:True,    #2    #je sors une de mes billes si W en bordure ou E à l'exterieur du plateau
					[symbol,opponent(symbol),'E'],         #:True,    #3    #je sors une bille adverse
					[symbol,opponent(symbol),opponent(symbol)],         #:False,   #4    #je ne peux pas bouger
					[symbol,symbol,symbol],         #:False,   #5    #je ne peux pas bouger
					[symbol,symbol,opponent(symbol),'E'],     #:True,    #6    #je sors une bille adverse
					[symbol,symbol,opponent(symbol),opponent(symbol),'E'], #:True,    #7    #je sors une bille adverse
					[symbol,symbol,opponent(symbol),opponent(symbol),opponent(symbol)], #:False,   #8    #je ne peux pas bouger
					]

					#['E'],                 #:True,    #0
					#['B','E'],             #:True,    #1
					#['B','B','E'],         #:True,    #2
					#['B','W','E'],         #:True,    #3
					#['B','W','W'],         #:False,   #4
					#['B','B','B'],         #:False,   #5
					#['B','B','W','E'],     #:True,    #6
					#['B','B','W','W','E'], #:True,    #7
					#['B','B','W','W','W'], #:False,   #8
	return possibilities

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
	
	grid[4][0] = 'W'
	grid[4][1] = 'B'
	grid[4][2] = 'B'
	grid[4][3] = 'W'
	grid[3][1] = 'W'

	result=findMove(grid,(4,2),'B')
	show(grid)
	print(result)

			
	

