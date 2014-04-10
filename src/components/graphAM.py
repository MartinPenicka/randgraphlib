
from components import Graph

class GraphAM(Graph):
    
    def __init__(self, num_nodes):
        Graph.__init__(self, num_nodes)
        
        self.repr_type = 'AM'
        self.graph = [[0] * self.num_nodes for _ in range(self.num_nodes)]
        
    def __str__(self):
        if self.graph == None:
            print "Graph not initialized"
            return
    
        str_repr = ""

        for row in self.graph:
            for col in row:
                str_repr += str(col) + " "
            str_repr += "\n"
        
        return str_repr
    
    def read(self, file_path):
        #TODO: Method for reading adjacencz matrices from file
        pass
    
    def write(self, file_path):
        #TODO: Method for writing adjacency matrices to files
        pass
    
    def add_node(self, number=1):
        #TODO: Method for adding new nodes to existing matrix
        pass
    
    def add_edge(self, start_node, end_node, value=1):
        if self.graph == None:
            print "Graph not initialized"
            return
        
        self.graph[start_node][end_node] = value
        
    def get_node_successors(self, node_idx):
        suc = []
        for node in range(self.num_nodes):
            if self.graph[node_idx][node] == 1:
                suc.append(node)
                
        return suc
    
#TODO: Write unittests for graphAM.py