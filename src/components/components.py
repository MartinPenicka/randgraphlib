

class Graph:
        
    def __init__(self, num_nodes):
        self.graph = None
        self.nodes = []
        self.num_nodes = num_nodes
        
        self.graph = [Node(_idx=x) for x in range(self.num_nodes)]   
            
    def __str__(self):
        pass
    
    def read(self, file_path):
        "reads graph from file,  format is read srom file first line"
        pass
    
    def write(self, file_path):
        "writes graph to file, adds format to start"
        pass
    
    def add_node(self, number = 1):
        pass
    
    def add_edge(self, start_node, end_node, value = 1):
        pass
    
    def get_node_successors(self, node_idx):
        pass
    

class Node:
    
    def __init__(self, _idx = 0):
        self.idx = _idx

class Edge:
    
    def __init__(self):
        self.n_from = None
        self.n_to = None
        self.directed = False