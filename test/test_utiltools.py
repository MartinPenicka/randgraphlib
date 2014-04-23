import unittest
from src.utiltools import *

class UtiltoolsTestCase(unittest.TestCase):
    
    def test_contains_same_value(self):
        
        self.assertTrue(contains_same_value([0,1,2], [5,8,9,4,7,7,7,2,3,9]))
        self.assertFalse(contains_same_value([1,1,1,1,], [2,3,5,8,9]))
        
    def test_recursive_contains(self):
        
        a = [1,2,3,4,5]
        b = [[1,2],[3,4],5]
        c = [[1,2,[3,[4]],5]]
        
        self.assertTrue(recursive_contains(a, 3))
        self.assertTrue(recursive_contains(b, 3))
        self.assertTrue(recursive_contains(c, 3))
        self.assertFalse(recursive_contains(c, 7))
        self.assertTrue(recursive_contains(c, 4))
        self.assertFalse(recursive_contains(a, 7))
        self.assertFalse(recursive_contains(b, 7))
        
if __name__ == '__main__':
    unittest.main()