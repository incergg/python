from game import TicTacToe
from minimax import AI
import unittest
import sys
class TestGame(unittest.TestCase):
	def setUp(self):
		self.game1 = TicTacToe()
		self.game2 = TicTacToe([['X',0,0],[0,'O',0],[0,0,'X']])
		self.game3 = TicTacToe([['X','X','O'],['O','O',0],['O','X','X']])
		self.game4 = TicTacToe([['X','X','O'],['O','O','X'],['X','X','O']])
		self.ai1 = AI(self.game1)
	def test_init(self):
		self.assertEqual(self.game2.board[0][0], 'X')
		self.assertEqual(self.game1.board, [[0,0,0],[0,0,0],[0,0,0]])
		
		
	def test_makeMove(self):
		self.game1.makeMove(1,1,'X'),
		self.assertEqual(self.game1.board[1][1],'X')
		self.game2.makeMove(0,0,'O'),
		self.assertEqual(self.game2.board[0][0],'X')
		
	def test_deleteMove(self):
		self.game1.deleteMove(1,1),
		self.assertEqual(self.game1.board[1][1],0)

	def test_reset(self):
		self.game2.reset()
		self.assertEqual(self.game2.board, [[0,0,0],[0,0,0],[0,0,0]])

	def test_checkStatus(self):
		self.assertEqual(self.game2.checkStatus(), 1)
		self.assertEqual(self.game3.checkStatus(), 'O')
		self.assertEqual(self.game4.checkStatus(), -1)
		
	def test_getDepth(self):
		self.assertEqual(self.game1.getDepth(), 9)
		self.assertEqual(self.game2.getDepth(), 6)
		
	def test_avaliableMoves(self):
		self.assertEqual(self.game3.avaliableMoves(), [[1,2]])
		self.assertEqual(self.game2.avaliableMoves(), [[0,1],[0,2],[1,0],[1,2],[2,0],[2,1]])
		
	def test_outcome(self):
		self.assertEqual(self.ai1.outcome(self.game3.board), 1)
		self.assertEqual(self.ai1.outcome(self.game4.board), 0)
		
	def test_findMoves(self):
		self.assertEqual(self.ai1.findMoves(self.game3.board), [[1,2]])
		self.assertEqual(self.ai1.findMoves(self.game2.board), [[0,1],[0,2],[1,0],[1,2],[2,0],[2,1]])
	
	def test_getMove(self):
		self.ai2 = AI(TicTacToe([[0,0,'X'],[0,0,0],[0,0,0]]))
		self.assertEqual(self.ai2.getMove(), (1,1))
		self.ai3 = AI(TicTacToe([['X',0,'X'],[0,'O',0],[0,0,0]]))
		self.assertEqual(self.ai3.getMove(), (0,1))
		
	
if __name__ == '__main__':
	unittest.main(argv=['first-arg-is-ignored'], exit=False)
	