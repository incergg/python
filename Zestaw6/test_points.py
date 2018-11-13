import points
import unittest


class TestPoint(unittest.TestCase):



    def test_init(self):
    	test = points.Point(3,1)
    	self.assertIs(3, test.x)
    	self.assertIs(1, test.y)

    def test_str(self):
    	test = points.Point(2,5)
    	self.assertEqual("(2, 5)", str(test))

    def test_repr(self):
    	test = points.Point(3,2)
    	self.assertEqual("Point(3, 2)", repr(test))

    def test_eq(self):
    	test = points.Point(3,3)
    	self.assertTrue(test == points.Point(3,3))
    	self.assertFalse(test == points.Point(3,2))

    def test_ne(self):
    	test = points.Point(3,3)
    	self.assertTrue(test != points.Point(3,2))
    	self.assertFalse(test != points.Point(3,3))

    def test_add(self):
    	test = points.Point(3,1)
    	test2 = points.Point(-3,2)
    	test3 = points.Point(2,1)
    	res1 = points.Point(0,3)
    	res2 = points.Point(5,2)
    	res3 = points.Point(-1,3)
    	self.assertEqual(test + test2, res1)
    	self.assertEqual(test + test3, res2)
    	self.assertEqual(test2 + test3, res3)
    
    def test_sub(self):
    	test = points.Point(3,1)
    	test2 = points.Point(-3,2)
    	test3 = points.Point(2,1)
    	res1 = points.Point(6,-1)
    	res2 = points.Point(1,0)
    	res3 = points.Point(-5,1)
    	self.assertEqual(test - test2, res1)
    	self.assertEqual(test - test3, res2)
    	self.assertEqual(test2 - test3, res3)

    def test_mul(self):
    	test = points.Point(3,1)
    	test2 = points.Point(-3,2)
    	test3 = points.Point(2,1)
    	self.assertEqual(test * test2, -7)
    	self.assertEqual(test * test3, 7)
    	self.assertEqual(test2 * test3, -4)


    def test_cross(self):
    	test = points.Point(3,1)
    	test2 = points.Point(-3,2)
    	test3 = points.Point(2,1)
    	self.assertEqual(test.cross(test2), 9)
    	self.assertEqual(test.cross(test3), 1)
    	self.assertEqual(test2.cross(test3), -7)

    def test_length(self):
    	test = points.Point(4,3)
    	test2 = points.Point(-3,0)
    	self.assertEqual(test.length(), 5)
    	self.assertEqual(test2.length(), 3)




if __name__ == '__main__':
	unittest.main()