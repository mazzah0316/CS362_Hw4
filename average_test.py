import unittest
import average

class testAverage(unittest.TestCase):
    def test1(self):
        self.assertEqual(average.average([1, 2, 3]), 2)
        
    def test2(self):
        self.assertEqual(average.average([-1, -2, -3]), -2)
        
    def test3(self):
        self.assertEqual(average.average([]), 0)


if __name__ == '__main__':
    unittest.main()