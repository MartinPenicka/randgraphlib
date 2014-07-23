

class Graph:
        
    def __init__(self, num_nodes, directed):
        self.graph = None
        self.num_nodes = num_nodes
        self.directed = directed
        
        #self.graph = [Node(_idx=x) for x in range(self.num_nodes)]   
            
    def __str__(self):
        return ""
    
    def read(self, file_path):
        "reads graph from file,  format is read from file first line"
        pass
    
    def write(self, file_path):
        "writes graph to file, adds format to start"
        pass
    
    def plot_to_file(self, file_path):
        "Plots graph to png file using pygraphviz library."
        pass
    
    def plot(self):
        pass
    
    def write_dot(self, file_path):
        "Writes graph to file using dot language (graphviz library format)"
        pass
    
    def add_node(self, number = 1):
        pass
    
    def remove_node(self, node_idx):
        pass
    
    def add_edge(self, start_node, end_node, value = 1):
        pass
    
    def remove_edge(self, start_node, end_node):
        pass
    
    def get_node_successors(self, node_idx):
        pass
    

class Node:
    
    def __init__(self, _idx = 0):
        self.idx = _idx
        self.neighbours = []

class Edge:
    
    def __init__(self):
        self.n_from = None
        self.n_to = None
        self.directed = False