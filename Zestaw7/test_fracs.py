import unittest
from fracs import Frac

class TestFrac(unittest.TestCase):

    def setUp(self):
        self.frac1 = Frac(2,3)
        self.frac2 = Frac(4,3)
        self.frac3 = Frac(2,1)
        self.frac4 = Frac(0,3)
        self.frac5 = Frac(-2,5)
    def test_init(self):
        with self.assertRaises(ValueError):
            Frac(1,0)
        self.assertEqual(self.frac1.x, 2)
        self.assertEqual(self.frac4.y, 3)

    def test_str(self):
        self.assertIsInstance(str(self.frac1), str)
        self.assertEqual(str(self.frac2), "4/3")

    def test_repr(self):
        self.assertIsInstance(repr(self.frac1), str)
        self.assertEqual(repr(self.frac1), "Frac(2, 3)")

    def test_cmp(self):
        self.assertEqual(self.frac1 == self.frac1, True)
        self.assertEqual(self.frac1 == self.frac2, False)


    def test_add(self):
        self.assertEqual(repr(self.frac1+self.frac1), "Frac(4, 3)")
        self.assertEqual(repr(self.frac1 + (-self.frac2)), "Frac(-2, 3)")
        self.assertEqual(repr(self.frac4 + 1), "Frac(3, 3)")
        self.assertEqual(repr(1 + self.frac5), "Frac(3, 5)")

    def test_sub(self):
        self.assertEqual(repr(self.frac1-self.frac2), "Frac(-2, 3)")
        self.assertEqual(repr(self.frac2 -self.frac1), "Frac(2, 3)")
        self.assertEqual(repr(self.frac4 - 1), "Frac(-3, 3)")
        self.assertEqual(repr(1 - self.frac5), "Frac(7, 5)")

    def test_mul(self):
        self.assertEqual(repr(self.frac1*self.frac2), "Frac(8, 9)")
        self.assertEqual(repr(self.frac3*self.frac5), "Frac(-4, 5)")
        self.assertEqual(repr(self.frac1*2), "Frac(4, 3)")
        self.assertEqual(repr(2*self.frac1), "Frac(4, 3)")

    def test_div(self):
        self.assertEqual(repr(self.frac1/self.frac1), "Frac(6, 6)")
        self.assertEqual(repr(self.frac5/3), "Frac(-2, 15)")
        self.assertEqual(repr(2/self.frac5), "Frac(10, -2)")
        with self.assertRaises(ValueError):
            self.frac2 / 0

    def test_pos(self):
        self.assertEqual(+self.frac1, self.frac1)
        self.assertEqual(+self.frac3, self.frac3)
        self.assertEqual(self.frac1, self.frac1)

    def test_neg(self):
        self.assertEqual(repr(-self.frac1), "Frac(-2, 3)")
        self.assertEqual(repr(-self.frac2), "Frac(-4, 3)")
        self.assertEqual(repr(-self.frac3), "Frac(-2, 1)")

    def test_invert(self):
        self.assertEqual(repr(~self.frac1), "Frac(3, 2)")
        self.assertEqual(repr(-self.frac5), "Frac(2, 5)")

    def test_float(self):
        self.assertIsInstance(float(self.frac1), float)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()