from collections import defaultdict
import random
import time 
import move as mv
import efficiency
from copy import deepcopy

symbols = ['B', 'W']


def moves(state):               
	def getMarbleLocation(state,symbol):
		locations=[] 
		for i,line in enumerate(state['board']):
			for e,column in enumerate(line) :
				if (state['board'][i][e]==symbol):
					locations.append((i,e))
		return locations
	#print("in moves symbol",symbols[state['current']])
	marbles = getMarbleLocation(state,symbols[state['current']])
	allMoves=[]
	moves_marble=[]
	for marble in marbles:
		moves_marble = mv.findMove(state['board'],marble,symbols[state['current']])
		for elem in moves_marble:		
			allMoves.append(elem)
	return allMoves

def apply(state, move):            #to change state of grid use apply
	res=mv.moveMarblesTrain(state,move[0],move[1])
	return res

def random1(state):
	def getMarbleLocation(state,symbol):
		locations=[] 
		for i,line in enumerate(state['board']):
			for e,column in enumerate(line) :
				if (state['board'][i][e]==symbol):
					locations.append((i,e))
		return locations
	marbles = getMarbleLocation(state,symbols[state['current']])
	allMoves=[]
	moves_marble=[]
	for marble in marbles:
		moves_marble = mv.findMove(state['board'],marble,symbols[state['current']])
		for elem in moves_marble:		
			allMoves.append(elem)
	nextMove=random.sample(allMoves,1)
	print(nextMove)
	result={"response": "move",
	"move": {'marbles':nextMove[0][0],'direction':nextMove[0][1]},
	"message": "pass"}
	return result
	

def think(state):
	def getMarbleLocation(state,symbol):
		locations=[] 
		for i,line in enumerate(state['board']):
			for e,column in enumerate(line) :
				if (state['board'][i][e]==symbol):
					locations.append((i,e))
		return locations
	marbles = getMarbleLocation(state,symbols[state['current']])
	allMoves=[]
	moves_marble=[]
	for marble in marbles:
		moves_marble = mv.findMove(state['board'],marble,symbols[state['current']])
		for elem in moves_marble:		
			allMoves.append(elem)
	values=[]
	for move in allMoves:
		values.append(efficiency.valueOfMove(state,move,symbols[state['current']]))
	choice=max(values)
	moves=[]
	for i,value in enumerate(values) :
		if value == choice :
			moves.append(allMoves[i])
	nextMove=random.sample(moves,1)
	print(nextMove)
	#result={"response": "move",
	#"move": {'marbles':nextMove[0][0],'direction':nextMove[0][1]},
	#"message": "pass"}
	return nextMove

def think2(state):
	def getMarbleLocation(state,symbol):
		locations=[] 
		for i,line in enumerate(state['board']):
			for e,column in enumerate(line) :
				if (state['board'][i][e]==symbol):
					locations.append((i,e))
		return locations
	marbles = getMarbleLocation(state,symbols[state['current']])
	allMoves=[]
	moves_marble=[]
	for marble in marbles:
		moves_marble = mv.findMove(state['board'],marble,symbols[state['current']])
		for elem in moves_marble:		
			allMoves.append(elem)
	values=[]
	for move in allMoves:
		values.append(efficiency.valueOfMove(state,move,symbols[state['current']]))
	choice=max(values)
	moves=[]
	for i,value in enumerate(values) :
		if value == choice :
			moves.append(allMoves[i])
	nextMove=random.sample(moves,1)
	result={"response": "move",
	"move": {'marbles':nextMove[0][0],'direction':nextMove[0][1]},
	"message": "pass"}
	return result

def climb(state,depth):
	childs=[[]]
	player=0
	currentDepth=0
	movesValue=evaluateMove(state)
	for i,move in enumerate(movesValue):
		childs[0].append(move)
	state["current"]=(state["current"]+1)%2
	move=think(state)
	state=apply(state,move[0])
	state["current"]=(state["current"]+1)%2
	while currentDepth<depth:
		childs.append([])
		currentDepth=currentDepth+1
		for previous,previousState in enumerate(childs[currentDepth-1]) :																#je parcours tout les �tats � la profondeur currentDepth
			childs[currentDepth].append([])
			nextStateMoveValueList=evaluateMove(previousState[0])
			for indexState,newState in enumerate(nextStateMoveValueList):				#je calcule et �value tout les �tats possible � currentDepth +1
				childs[currentDepth][previous].append(nextStateMoveValueList)
	values={}
	value=0
	index=0
	for child in childs:
		for previous,previousState in enumerate(childs[currentDepth-1]) :
			for next,nextState in enumerate(childs[currentDepth]) :
				for elem in nextState:
					for x in elem:
						value=x[2]+previousState[2]
						values[i]=[x[2],previousState[1]]
						i+1
	maxValue=[]
	for key in values:
		maxValue.append(values[key][0])
	choice=max(maxValue)
	find=maxValue.index(choice)
	for i,key in enumerate(values):
		if i==find:
			result={"response": "move",
					"move": {'marbles':values[key][1][0],'direction':values[key][1][1]},
					"message": "pass"}
			return result
	return False

def evaluateMove(state):
	allMoves=[]
	for move in moves(state):
		valuesPreviousState=efficiency.valueOfState(state)
		newState={"players":deepcopy(state["players"]),"current":deepcopy(state["current"]),"board":deepcopy(state['board'])}
		newState=apply(newState,move)
		valuesNextState=efficiency.valueOfState(newState)
		value = efficiency.diff(valuesPreviousState,valuesNextState)
		allMoves.append([newState,move,value])
	return allMoves



if __name__=='__main__':
	state={'players': ['toto2', 'toto1'],
			'current': 0,
	  		'board': [['W', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X'],
	  			['W', 'W', 'W', 'W', 'W', 'W', 'X', 'X', 'X'],
	    		['E', 'E', 'W', 'W', 'W', 'E', 'E', 'X', 'X'],
		 		['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'X'],
		 		['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
		   		['X', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E'],
		    	['X', 'X', 'E', 'E', 'B', 'B', 'B', 'E', 'E'],
			 	['X', 'X', 'X', 'B', 'B', 'B', 'B', 'B', 'B'],
			  	['X', 'X', 'X', 'X', 'B', 'B', 'B', 'B', 'B']]
		}

	result=climb(state,1)
	print(result)

