
import unittest
import volume

class testVolume(unittest.TestCase):
    def test1(self):
        self.assertEqual(volume.volume(5.5), 166.375)
        
    def test2(self):
       self.assertRaises(TypeError, volume.volume, "hi")
        
    def test3(self):
        self.assertEqual(volume.volume(-10), 0)


if __name__ == '__main__':
    unittest.main()