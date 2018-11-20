import unittest
import rectangles
import points

class TestRectangle(unittest.TestCase):
	def test_init(self):
		test = rectangles.Rectangle(1,1,3,2)
		self.assertIs(test.pt1.x,1)
		self.assertIs(test.pt1.y,1)
		self.assertIs(test.pt2.x,3)
		self.assertIs(test.pt2.y,2)
		with self.assertRaises(ValueError):
			rectangles.Rectangle(3,4,2,7)
		with self.assertRaises(ValueError):
			rectangles.Rectangle(3,4,6,3)
	
	def test_str(self): 
		test = rectangles.Rectangle(1,1,3,2)
		self.assertEqual("[(1, 1), (3, 2)]", str(test))
	
	def test_repr(self):
		test = rectangles.Rectangle(1,1,3,2)
		self.assertEqual("Rectangle(1, 1, 3, 2)", repr(test))
	
	def test_eq(self):
		test = rectangles.Rectangle(1,1,3,2)
		self.assertTrue(test == rectangles.Rectangle(1,1,3,2))
		self.assertFalse(test == rectangles.Rectangle(1,2,3,2))
		self.assertFalse(test == rectangles.Rectangle(1,1,3,1))
		
	def test_ne(self): 
		test = rectangles.Rectangle(1,1,3,2)
		self.assertTrue(test != rectangles.Rectangle(1,2,3,2))
		self.assertFalse(test != rectangles.Rectangle(1,1,3,2))
		self.assertTrue(test != rectangles.Rectangle(1,1,3,1))
	
	def test_center(self):
		test = rectangles.Rectangle(1,1,3,2)
		self.assertEqual(test.center(),points.Point(2,1.5))
		
	def test_area(self):
		test = rectangles.Rectangle(1,1,3,2)
		self.assertEqual(test.area(),2)
		
	def test_move(self):
		test = rectangles.Rectangle(1,1,3,2)
		self.assertEqual(test.move(-1,2),rectangles.Rectangle(0, 3, 2, 4))

if __name__ == '__main__':
	unittest.main()