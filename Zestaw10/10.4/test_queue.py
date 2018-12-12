from queue import Queue
import unittest

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.empty = Queue(1)
        self.full = Queue(1)
        self.full.put(4)

    def test_init(self):
        self.test2 = Queue(1)
        self.assertEqual(self.test2.n, 2)
        self.assertEqual(self.test2.head, 0)
        self.assertEqual(self.test2.tail, 0)

    def test_is_empty(self):
        self.assertFalse(self.full.is_empty())
        self.assertTrue(self.empty.is_empty())
        
    def test_is_full(self):
        self.assertTrue(self.full.is_full())
        self.assertFalse(self.empty.is_full())

    def test_put(self):
        self.test = Queue(1)
        self.test.put(3)
        with self.assertRaises(ValueError):
            self.test.put(4)

    def test_get(self):
        self.test3 = Queue(1)
        self.test3.put(3)
        self.assertEqual(self.test3.get(), 3)
        with self.assertRaises(ValueError):
            self.test3.get()
            
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
