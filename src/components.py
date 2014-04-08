

class Graph:
        
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
        if self.graph == None:
            print "Graph not initialized"
            return
        
        str_repr = ""
        
        if self.mode == 1:
            pass
        
        elif self.mode == 2:
            for row in self.graph:
                for col in row:
                    str_repr += str(col) + " "
                str_repr += "\n"
                
        elif self.mode == 3:
            pass
        
        else:
            print "Error : invalid argument (mode, Graph module)"
            return ""
        
        return str_repr
    
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