

class Graph:
        
    def __init__(self, node_num, mode):
        self.graph = None
        self.nodes = []
        self.node_num = node_num
        self.mode = mode

        self._set_structure()
    
    def _set_structure(self):
        if self.node_num == 0:
            print "Error : number of nodes equal 0 (node_num, Graph module)"
            return
        
        self.graph = [Node(_idx=x) for x in range(self.node_num)]
        
        if self.mode == 0:
            pass
        elif self.mode == 1:
            self.graph = [[0] * self.node_num for _ in range(self.node_num)]
        elif self.mode == 2:
            pass
        else:
            print "Error : invalid argument (mode, Graph module)"
            
    def __str__(self):
        if self.graph == None:
            print "Graph not initialized"
            return
        
        str_repr = ""
        
        if self.mode == 0:
            pass
        
        elif self.mode == 1:
            for row in self.graph:
                for col in row:
                    str_repr += str(col) + " "
                str_repr += "\n"
                
        elif self.mode == 2:
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
    
    def add_node(self, number = 1):
        pass
    
    def add_edge(self, start_node, end_node, value = 1):
        if self.graph == None:
            print "Graph not initialized"
            return
        
        if self.mode == 0:
            pass
        
        elif self.mode == 1:
            self.graph[start_node][end_node] = value
                
        elif self.mode == 2:
            pass
        
        else:
            print "Error : invalid argument (mode, Graph module)"
            return
    

class Node:
    
    def __init__(self, _idx = 0):
        self.idx = _idx

class Edge:
    
    def __init__(self):
        self.n_from = None
        self.n_to = None
        self.directed = False