import unittest
from src.algorithms import split_to_components
from random_graphs import TestGraphs

class AlgorithmsTestCase(unittest.TestCase):
    '''
    Testf fo algorithms.py module
    '''
    
    def test_split_to_components(self):
        tg = TestGraphs()
        
        self.assertEquals(split_to_components(tg.fully_connected), [[0, 1, 2, 3, 4]])
        self.assertEquals(split_to_components(tg.fully_separated), [[0], [1], [2], [3], [4]])
        self.assertEquals(split_to_components(tg.common_graph), [[0], [1, 2, 3, 4]])
        
if __name__ == '__main__':
    unittest.main()