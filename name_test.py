  
import unittest
import name

class testName(unittest.TestCase):
    def test1(self):
        self.assertEqual(name.fullname("Hudson", "Mazza"), "Hudson Mazza")
        
    def test2(self):
        self.assertEqual(name.fullname(10, 20), "10 20")
        
    def test3(self):
        self.assertEqual(name.fullname("", ""), " ")


if __name__ == '__main__':
    unittest.main()