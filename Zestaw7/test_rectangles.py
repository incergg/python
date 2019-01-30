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
		
	def test_intersection(self):
		
		test1 = rectangles.Rectangle(1,1,3,2)
		test2 = rectangles.Rectangle(0,0,2,2)
		test3 = rectangles.Rectangle(3,1,4,2)
		test4 = rectangles.Rectangle(0,1.5,2,3)
		self.assertEqual(rectangles.Rectangle.intersection(test1,test2), rectangles.Rectangle(1,1,2,2))
		self.assertEqual(rectangles.Rectangle.intersection(test1,test3), rectangles.Rectangle(0,0,0,0))
		self.assertEqual(rectangles.Rectangle.intersection(test1,test4), rectangles.Rectangle(1,1.5,2,2))
		
	def test_cover(self):
		test1 = rectangles.Rectangle(1,1,3,2)
		test2 = rectangles.Rectangle(0,0,2,2)
		test3 = rectangles.Rectangle(3,1,4,2)
		test4 = rectangles.Rectangle(0,1.5,2,3)
		self.assertEqual(rectangles.Rectangle.cover(test1,test2), rectangles.Rectangle(0,0,3,2))
		self.assertEqual(rectangles.Rectangle.cover(test1,test3), rectangles.Rectangle(1,1,4,2))
		self.assertEqual(rectangles.Rectangle.cover(test1,test4), rectangles.Rectangle(0,1,3,3))
		
	def test_make4(self):
		test2 = rectangles.Rectangle(0,0,2,2)
		self.assertEqual(rectangles.Rectangle.make4(test2)[0], rectangles.Rectangle(0,0,1,1) )
		self.assertEqual(rectangles.Rectangle.make4(test2)[1], rectangles.Rectangle(0,1,1,2) )
		self.assertEqual(rectangles.Rectangle.make4(test2)[2], rectangles.Rectangle(1,1,2,2) )
		self.assertEqual(rectangles.Rectangle.make4(test2)[3], rectangles.Rectangle(1,0,2,2) )
		
if __name__ == '__main__':
	unittest.main()