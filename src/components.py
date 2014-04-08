

class Graph:
    
    '''
    Graph mode :
        1 - adjacency list
        2 - adjacency matrix
        3 - object representation
        
    Number of nodes n
        
    Edge probability :
        for each two nodes is edge inserted by this probability, 1 = full graph
        
    Continuous graph :
        0/1 - if 1, checks graph if all nodes are connected, if not, generates randomly new edge
        
    Multigraph :
        n - if not zero, inserts n edges for every tuple of nodes, single edge with given probability
    '''
    
    
    def __init__(self, nodes = 0, mode = 3, edge_prob = 0.1, cont = 0, multi_g = 0):
        self.node_list = []
        self.edge_list = []
        self.mode = mode
        self.edge_prob = edge_prob
        self.cont = cont
        self.multi_g = multi_g

class Node:
    
    def __init__(self, _idx = 0):
        self.idx = _idx

class Edge:
    
    def __init__(self):
        self.n_from = None
        self.n_to = None
        self.directed = False