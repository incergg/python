from stack import Stack
import unittest

class TestStac(unittest.TestCase):
	
	def setUp(self):
		self.empty = Stack()
		self.full = Stack(1)
		self.full.push(1)
		self.test1 = Stack(10)
		
	def test_init(self):
		self.test2 = Stack(2)
		self.assertEqual(self.test2.size, 2)
		self.assertEqual(self.test2.n, 0)
	
	def test_is_empty(self):
		self.assertTrue(self.empty.is_empty())
		self.assertFalse(self.full.is_empty())
	
	def test_is_full(self):
		self.assertFalse(self.empty.is_full())
		self.assertTrue(self.full.is_full())
	
	def test_push(self):
		self.test1.push(3)
		self.assertEqual(1, self.test1.n)
		self.assertEqual(3, self.test1.items[0])
		with self.assertRaises(ValueError):
			self.full.push(3)
	
	def test_pop(self):
		self.test1.push(3)
		self.assertEqual(self.test1.pop(), 3)
		with self.assertRaises(ValueError):
			self.empty.pop()
	
if __name__ == '__main__':
	unittest.main()
