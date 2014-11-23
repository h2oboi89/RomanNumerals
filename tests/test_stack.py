import unittest
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from stack import Stack

class StackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        
    def test_isEmpty(self):
        self.assertTrue(self.stack.isEmpty())
        
        self.stack.push(1)
        
        self.assertFalse(self.stack.isEmpty())
        
    def test_push_and_pop(self):
        val = 1
        
        self.stack.push(val)
        self.assertFalse(self.stack.isEmpty())
        self.assertEqual(val, self.stack.pop())
        self.assertTrue(self.stack.isEmpty())
        
    def test_peek(self):
        self.assertIsNone(self.stack.peek())
        
        val = 1
        
        self.stack.push(val)
        self.assertFalse(self.stack.isEmpty())
        self.assertEqual(val, self.stack.peek())
        self.assertFalse(self.stack.isEmpty())
    
    def test_size(self):
        self.assertEqual(0, self.stack.size())
        
        self.stack.push(1)
        
        self.assertEqual(1, self.stack.size())
        
    def test_clear(self):
        self.stack.push(1)
        
        self.stack.clear()
        
        self.assertTrue(self.stack.isEmpty())
        
    def test_str(self):
        self.assertEqual('{}', str(self.stack))
               
        self.stack.push(1)
        
        self.assertEqual('{1}', str(self.stack))
        
        self.stack.push(2)
        
        self.assertEqual('{1, 2}', str(self.stack))
    
    def test_advanced(self):
        self.assertTrue(self.stack.isEmpty())
        
        for i in range(5):
            self.assertEqual(i, self.stack.size())
            self.stack.push(i)
            self.assertEqual(i, self.stack.peek())
            
        for i in range(4,-1, -1):
            self.assertEqual(i + 1, self.stack.size())
            self.assertEqual(i, self.stack.pop())
        
        self.assertTrue(self.stack.isEmpty())
        
        self.assertIsNone(self.stack.peek())
        self.assertIsNone(self.stack.pop())
    
if __name__ == '__main__':
    unittest.main()