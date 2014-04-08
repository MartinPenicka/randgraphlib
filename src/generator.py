
import components as cmpn

class Graphgen:
    
    def __init__(self):
        pass
    
    def gen_common(self, node_num, edge_num, directed):
        
        graph = cmpn.Graph()
        
        for node in range(node_num):
            graph.node_list.append(cmpn.Node(node))