from components import Graph, Node
import pygraphviz as pgv

class MyNode(Node):
    
    def __init__(self, _idx=0):
        Node.__init__(self, _idx=_idx)
        
    def add_neighbour(self, node):
        self.neighbours.append(node)
        node.neighbours.append(self)
    
    def delete_neighbour(self, node):
        for n in self.neighbours:
            if n.idx == node.idx:
                tmp_node = n
                self.neighbours.remove(n)
                break
            
        for n in tmp_node.neighbours:
            if n.idx == self.idx:
                tmp_node.neighbours.remove(n)
    
    def has_neighbour(self, node):
        for n in self.neighbours:
            if n.idx == node.idx:
                return True
            
        return False

class GraphNodes(Graph):
    
    def __init__(self, num_nodes, directed):
        Graph.__init__(self, num_nodes, directed)
        
        self.graph = [MyNode(_idx = x) for x in range(self.num_nodes)]
        
    def __str__(self):
        return ""
    
    def read(self, file_path):
        pass
    
    def write(self, file_path):
        pass
    
    def _create_pgv_object(self, update = False):
        
        if hasattr(self, 'pgv_object') and not update:
            return
        
        if self.directed == 1:
            self.pgv_object = pgv.AGraph(directed = True)
        else:
            self.pgv_object = pgv.AGraph(directed = False)
            
        for node in self.graph:
            self.pgv_object.add_node(str(node.idx))
            
        for node in self.graph:
            for neighbour in node.neighbours:
                self.pgv_object.add_edge(str(node.idx), str(neighbour.idx))
    
    def plot_to_file(self, file_path):
        
        self._create_pgv_object()
        
        self.pgv_object.graph_attr.update(size="50!")
        self.pgv_object.layout()
        self.pgv_object.draw(file_path)
    
    def plot(self):
        pass
    
    def write_dot(self, file_path):
        pass
    
    def add_node(self, number = 1):
        self.graph.append(MyNode(_idx = self.num_nodes))
        self.num_nodes += 1
    
    def remove_node(self, node_idx):
        if node_idx >= self.num_nodes:
            print "Parameter node_idx bigger than number of nodes in graph."
            return
        
        idx_to_delete = -1
        for i,node in enumerate(self.graph):
            if node.idx == node_idx:
                idx_to_delete = i
                break
        
        for node in self.graph:
            for n in node.neighbours:
                if n.idx == node_idx:
                    node.neighbours.remove(n)
                    break
        self.graph.pop(idx_to_delete)
        
    
    def add_edge(self, start_node, end_node, value = 1):
        
        first_node = None
        second_node = None
        
        for node in self.graph:
            if node.idx == start_node:
                first_node = node
            elif node.idx == end_node:
                second_node = node
                
            if first_node != None and second_node != None:
                first_node.add_neighbour(second_node)
                return
    
    def get_node_successors(self, node_idx):
        for node in self.graph:
            if node.idx == node_idx:
                return [n.idx for n in node.neighbours]
            
    def get_average_node_degree(self):
        
        average_deg_sum = 0
        for node in self.graph:
            average_deg_sum += len(node.neighbours)
            
        return average_deg_sum / len(self.graph)