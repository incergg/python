import time 
from random import randint
from os import system
from minimax import AI
import sys

class TicTacToe:
	def __init__(self, board = [[0,0,0],[0,0,0],[0,0,0]]):
		self.board = board
		self.players = ['X','O',0]
		self.coords = {
			1: [0, 0], 2: [0, 1], 3: [0, 2],
			4: [1, 0], 5: [1, 1], 6: [1, 2],
			7: [2, 0], 8: [2, 1], 9: [2, 2],
		}
		
	def makeMove(self, x,y, player):
		if self.isMoveValid(x,y):
			self.board[x][y] = player
	
	def deleteMove(self,x,y):
		self.board[x][y] = 0
		
	def isMoveValid(self,x,y):
		if self.board[x][y] == 0:
			return True
		else:
			return False
			
		
	def reset(self):
		for x in range(3):
			for y in range(3):
				self.deleteMove(x,y)
				
	def checkStatus(self, state = None, flag=False):
		if flag == False:
			state = self.board
		if state[0][0]==state[0][1]==state[0][2] != 0:
			return state[0][0]
		if state[1][0]==state[1][1]==state[1][2] != 0:
			return state[1][0]
		if state[2][0]==state[2][1]==state[2][2] != 0:
			return state[2][0]
		if state[0][0]==state[1][0]==state[2][0] != 0:
			return state[0][0]
		if state[0][1]==state[1][1]==state[2][1] != 0:
			return state[0][1]
		if state[0][2]==state[1][2]==state[2][2] != 0:
			return state[0][2]
		if state[0][0]==state[1][1]==state[2][2] != 0:
			return state[0][0]
		if state[2][0]==state[1][1]==state[0][2] != 0:
			return state[0][2]
		
		if self.getDepth() == 0:
			"""Remis"""
			return -1
		return 1 
		"""KONTYNUJ GRE """

	def getDepth(self):
		i = 0
		for x in self.board:
			for y in x:
				if y == 0:
					i+=1
		return i
		
	def draw(self):
		print('\n---------------')
		for x in self.board:
			for y in x:
				if y != 0:
					print('| '+str(y)+ ' |', end='')
				else:
					print('|   |', end='')
			print('\n---------------')	
	

	def play(self):	
		if self.checkStatus() != 1:
			return 
		
		choice = ''
		while choice == '':
			try:
				choice = int(input("\n Wybierz pozycje [1-9]: "))
				if choice<1 or choice > 9:
					print("\n Pozycja niedozwolona")
					self.draw()
					choice =''
				else:
					move = self.coords[choice]
					
					if self.isMoveValid(move[0],move[1]):
						self.makeMove(move[0],move[1], 'X')
					else:
						print("\n  Pozycja zajeta!!!")
						self.draw()
						choice = ''
			except(KeyError, ValueError):
				print ("\n  Podaj wolna pozycje [1-9]!!!")
				self.draw()
				choice=''
				
	def avaliableMoves(self):
		moves = []
		i=0
		for x in self.board:
			j=0
			for y in x:
				if y == 0:
					moves.append([i,j])
				j+=1
			i+=1
		return moves
		
	def autoPlay(self):
		if self.checkStatus() != 1:
			return 
		moves = self.avaliableMoves()
		x = randint(0,len(moves)-1)

		move = moves[x]
		self.makeMove(move[0],move[1],'X')
		time.sleep(0.5)

	def computerPlay(self, computer):
		if self.checkStatus() != 1:
			return 

		move = computer.getMove()
		self.makeMove(move[0], move[1], 'O')
		time.sleep(0.5)
		

		


def main (autoPlayFlag = 0, firstFlag = -1):
	
	game = TicTacToe()
	game.reset()
	first = ''
	if firstFlag != -1:
		if firstFlag == 0:
			first = 'N'
		else:
			first = 'T'

		
	
		
	system('cls')
	print ("\n	Witaj w grze kolko i krzyzyk!	\n")
	game.draw()
	while first != 'T' and first != 'N':
		try:
			first = input('\nCzy wykonujesz pierwszy ruch? [T/N]: ').upper()
			if  first != 'T' and first != 'N':
				print ("\n	Podaj [N] - NIE lub [T] - TAK!!!")
				game.draw()
		except(EOFError, KeyboardInterrupt):
			print ( "\n\n	Dzieki za gre! :)")
			exit()
	A = AI(game)		
	if first == 'N':
		system('cls')
		print ("\n	Witaj w grze kolko i krzyzyk!	\n")
		print ("\n Tura 'O': ")
		game.draw()
		game.computerPlay(A)
		
	while game.checkStatus() == 1:
		try:
			system('cls')
			print ("\n	Witaj w grze kolko i krzyzyk!	\n")
			print ("\n Tura 'X': ")
			game.draw()

			if autoPlayFlag == 1:
				game.autoPlay()
			else:
				game.play()
			A  = AI (game)
			if  game.checkStatus() == 1:
				system('cls')
				print ("\n	Witaj w grze kolko i krzyzyk!	\n")
				print ("\n Tura 'O': ")
				game.draw()
				game.computerPlay(A)
				
		except(EOFError, KeyboardInterrupt):
			print ( "\n\n	Dzieki za gre! :)")
			exit()
	system('cls')
	print ("\n	Witaj w grze kolko i krzyzyk!	\n")
	game.draw()	
	if game.checkStatus() == -1:
		print ( '\n	REMIS!		')
	else:
		print ('\n	Zwyciezca: ', game.checkStatus(),'		')
	

	

if(len(sys.argv) == 1):
	main()
if(len(sys.argv) == 2):
	if int(sys.argv[1]) == 2:
		pass
	else:
		main(int(sys.argv[1]))	
	
if(len(sys.argv) == 3):
	main(int(sys.argv[1]),int(sys.argv[2]))				
						
if(len(sys.argv) == 4):
	i = int(sys.argv[3])
	if i>999:
		i = 999
	for x in range(0,i):	
		main(int(sys.argv[1]),int(sys.argv[2]))
		time.sleep(2)

	