import unittest
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from main import r_to_d

class RDTestCase(unittest.TestCase):
    def test_i(self):
        self.assertEqual(1, r_to_d('I'))
        self.assertEqual(2, r_to_d('II'))
        self.assertEqual(3, r_to_d('III'))
        
    def test_v(self):
        self.assertEqual(4, r_to_d('IV'))
        self.assertEqual(5, r_to_d('V'))
        self.assertEqual(6, r_to_d('VI'))
        self.assertEqual(7, r_to_d('VII'))
        self.assertEqual(8, r_to_d('VIII'))
        
    def test_x(self):
        self.assertEqual(9, r_to_d('IX'))
        self.assertEqual(10, r_to_d('X'))
        self.assertEqual(11, r_to_d('XI'))
        self.assertEqual(12, r_to_d('XII'))
        self.assertEqual(13, r_to_d('XIII'))
        
    def test_teens(self):
        self.assertEqual(14, r_to_d('XIV'))
        self.assertEqual(15, r_to_d('XV'))
        self.assertEqual(16, r_to_d('XVI'))
        self.assertEqual(17, r_to_d('XVII'))
        self.assertEqual(18, r_to_d('XVIII'))
        self.assertEqual(19, r_to_d('XIX'))
        
    def test_twenties(self):
        self.assertEqual(20, r_to_d('XX'))
        self.assertEqual(21, r_to_d('XXI'))
        self.assertEqual(22, r_to_d('XXII'))
        self.assertEqual(23, r_to_d('XXIII'))
        self.assertEqual(24, r_to_d('XXIV'))
        self.assertEqual(25, r_to_d('XXV'))
        self.assertEqual(26, r_to_d('XXVI'))
        self.assertEqual(27, r_to_d('XXVII'))
        self.assertEqual(28, r_to_d('XXVIII'))
        self.assertEqual(29, r_to_d('XXIX'))
        
    def test_reference(self):
        self.assertEqual(12, r_to_d('xii'))
        self.assertEqual(1776, r_to_d('mdcclxxvi'))
        self.assertEqual(9, r_to_d('ix'))
        self.assertEqual(94, r_to_d('xciv'))
        self.assertEqual(4, r_to_d('iv'))
        self.assertEqual(34, r_to_d('XXXIV'))
        self.assertEqual(267, r_to_d('CCLXVII'))
        self.assertEqual(764, r_to_d('DCCLXIV'))
        self.assertEqual(987, r_to_d('CMLXXXVII'))
        self.assertEqual(1983, r_to_d('MCMLXXXIII'))
        self.assertEqual(2014, r_to_d('MMXIV'))
        self.assertEqual(4000, r_to_d('MMMM'))
        self.assertEqual(4999, r_to_d('MMMMCMXCIX'))
    
if __name__ == '__main__':
    unittest.main()