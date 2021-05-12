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

	result=findMove(grid,(2,2),'W')
	show(grid)
	print(result)

			
	

