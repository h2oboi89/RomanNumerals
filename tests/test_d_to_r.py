import unittest
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from main import d_to_r

class DRTestCase(unittest.TestCase):
    def test_fail(self):
        self.assertEqual('', d_to_r(0))
        self.assertEqual('', d_to_r(5000))

    def test_i(self):
        self.assertEqual('I', d_to_r(1))
        self.assertEqual('II', d_to_r(2))
        self.assertEqual('III', d_to_r(3))
        
    def test_v(self):
        self.assertEqual('IV', d_to_r(4))
        self.assertEqual('V', d_to_r(5))
        self.assertEqual('VI', d_to_r(6))
        self.assertEqual('VII', d_to_r(7))
        self.assertEqual('VIII', d_to_r(8))
        
    def test_x(self):
        self.assertEqual('IX', d_to_r(9))
        self.assertEqual('X', d_to_r(10))
        self.assertEqual('XI', d_to_r(11))
        self.assertEqual('XII', d_to_r(12))
        self.assertEqual('XIII', d_to_r(13))
    
if __name__ == '__main__':
    unittest.main()