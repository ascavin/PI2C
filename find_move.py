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
		alignement.clear()
		while find and e<5:           
			#print("neighbor",(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e),neighbor(grid,(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e)))
			alignement.append(neighbor(grid,(marble[0]+directions[direction][0]*e,marble[1]+directions[direction][1]*e)))
			possibilities=getPossibilities(symbol)
			for i,possibilitie in enumerate(possibilities):
				#print(alignement)	 
				#print("i",i) 
				# if i == 7:
				# 	print(possibilitie)   
				# 	print("-------------------------")

				#if direction =='W':			
					#print("possibilitie",possibilitie)
					#print("alignement",alignement) 
				if possibilitie == alignement :					
					find=False
										
					if i == 0: 
						moves.append([[[marble[0],marble[1]]],direction])
					if i == 1:
						pass
					if i == 2: 
						moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]]],direction])
					if i==3:
						pass
					if i == 4:
						moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]],[marble[0]+directions[direction][0]*2,marble[1]+directions[direction][1]*2]],direction])
					if i == 5:
						pass
					if (i == 6):
						moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]]],direction])
					if i == 7:
						print("find7")
						moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]]],direction])			
					if i == 8:
						pass
					if i == 9:
						pass
					if i == 10 or i==11:
						moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]],[marble[0]+directions[direction][0]*2,marble[1]+directions[direction][1]*2]],direction])
					
					if i == 12 or i==13:
						moves.append([[[marble[0],marble[1]],[marble[0]+directions[direction][0],marble[1]+directions[direction][1]],[marble[0]+directions[direction][0]*2,marble[1]+directions[direction][1]*2]],direction])
					if i == 14:
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
					[symbol,'E'],            			 #:True,    #2    
					[symbol,'X'],						#False,		#3
					[symbol,symbol,'E'],         			#:True,    #4    
					[symbol,symbol,'X'],					#False,		#5
					[symbol,opponent(symbol),'E'],        			#:True,    #6    #je sors une bille adverse
					[symbol,opponent(symbol),'X'],					#:True 		#7
					[symbol,opponent(symbol),opponent(symbol)],        					#:False,   #8    #je ne peux pas bouger
					[symbol,symbol,symbol],        					 					#:False,   #9    #je ne peux pas bouger
					[symbol,symbol,opponent(symbol),'E'],     							#:True,    #10    #je sors une bille adverse
					[symbol,symbol,opponent(symbol),'X'],								#:True, 	#11
					[symbol,symbol,opponent(symbol),opponent(symbol),'E'], 				#:True,    #12    #je sors une bille adverse
					[symbol,symbol,opponent(symbol),opponent(symbol),'X'],				#:True 		#13
					[symbol,symbol,opponent(symbol),opponent(symbol),opponent(symbol)], #:False,   #14    #je ne peux pas bouger
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
	#grid[4][3] = 'B'
	#grid[4][4] = 'W'
	#grid[3][1] = 'W'

	result=findMove(grid,(4,2),'B')
	show(grid)
	print(result)

			
	

