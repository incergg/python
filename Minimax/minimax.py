from random import randint
from os import system

class AI:
	def __init__(self, gameinstance):
		self.game =  gameinstance
		self.state = gameinstance.board
		
		
		
	def outcome(self, state):
		if self.game.checkStatus(state, True) == 'O':
			return 1
		elif self.game.checkStatus(state, True) == 'X':
			return -1
		return 0
		
	def findMoves(self, state):
		moves = []
		i=0
		for x in state:
			j=0
			for y in x:
				if y == 0:
					moves.append([i,j])
				j+=1
			i+=1
		return moves	


	def minimax(self, state, depth, player):
		move = [-1,-1]
		if player == 'O':	
			best = -100
	
		else:
			best = 100
	
		if self.game.checkStatus(state, True) != 1:
			score = self.outcome(state)
			return score, [-1,-1]
		
		for cord in self.findMoves(state):
			x, y = cord[0], cord[1]
			state[x][y] = player
			if player == 'O':
				score, lastMove = self.minimax(state, depth - 1, 'X')
			else:
				score, lastMove = self.minimax(state, depth - 1 , 'O')
			state[x][y] = 0
			lastMove[0], lastMove[1] = x,y
			
		
			if player == 'O':
				if score > best:
					best = score # max value
					move = lastMove
			else:
				if score < best:
					best = score # min value
					move = lastMove
		return best, move
	
	def getMove (self):
		tmove = [-1,-1]
		if self.game.checkStatus(self.state, True) != 1:
			return
		if len(self.findMoves(self.state)) == 9:
			x = randint(0,2)
			y = randint(0,2)
		else:
			score, tmove = self.minimax(self.state, len(self.findMoves(self.state)), 'O')
		
		return tmove[0],tmove[1]

	
