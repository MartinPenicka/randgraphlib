

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
        
    Directed : 0/1
    '''
    
    
    def __init__(self, node_num = 10, mode = 3, edge_prob = 0.1, cont = 0, multi_g = 0, directed = 0):
        self.graph = None
        self.node_num = node_num
        self.mode = mode
        self.edge_prob = edge_prob
        self.cont = cont
        self.multi_g = multi_g
        self.directed = directed
        
        self._set_structure()
    
    def _set_structure(self):
        if self.node_num == 0:
            print "Error : number of nodes equal 0 (node_num, Graph module)"
            return
        
        if self.mode == 0:
            self.graph = [Node(_idx=x) for x in range(self.node_num)]
        elif self.mode == 1:
            self.graph = [[0] * self.node_num for _ in range(self.node_num)]
        elif self.mode == 2:
            self.graph = [Node(_idx=x) for x in range(self.node_num)]
        else:
            print "Error : invalid argument (mode, Graph module)"
            
    def __str__(self):
        "print method of graph"
    
    def read(self, file_path):
        "reads graph from file,  format is read srom file first line"
        pass
    
    def write(self, file_path):
        "writes graph to file, adds format to start"
        pass
    

class Node:
    
    def __init__(self, _idx = 0):
        self.idx = _idx

class Edge:
    
    def __init__(self):
        self.n_from = None
        self.n_to = None
        self.directed = False