
from components import Graph

class GraphAM(Graph):
    
    def __init__(self, node_num):
        Graph.__init__(self, node_num)
        
        self.repr_type = 'AM'
        self.graph = [[0] * self.node_num for _ in range(self.node_num)]
        
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
        pass
    
    def write(self, file_path):
        pass
    
    def add_node(self, number=1):
        pass
    
    def add_edge(self, start_node, end_node, value=1):
        if self.graph == None:
            print "Graph not initialized"
            return
        
        self.graph[start_node][end_node] = value