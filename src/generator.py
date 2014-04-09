
from components import graphAM as g
import random as r
import cfg

class Graphgen:
    
    def __init__(self):
        self.graph = None
    
    def set_graph(self, graph):
        self.graph = graph
    
    def generate(self, cfg):
        
        #TODO: graph module must not depend on representation
        if self.graph == None:
            self.graph = g.GraphAM(cfg.num_nodes)
        
        for node in range(self.graph.node_num):
            for node2 in range(self.graph.node_num):
                if node == node2 and cfg.loops == 0:
                    continue
                
                # add new edge
                if r.random() < cfg.edge_prob:
                    
                    weight = self._get_wight()
                    
                    self.graph.add_edge(node, node2, weight)
                    if cfg.directed == 0:
                        self.graph.add_edge(node2, node, weight)
                    
                    if cfg.multi_g > 0 and self.graph.repr_type != 'AM':
                        for _ in range(cfg.multi_g):
                            if r.random() < cfg.multi_g_edge_prob:
                                weight = self._get_wight()
                                
                                self.graph.add_edge(node, node2, weight)
                                if cfg.directed == 0:
                                    self.graph.add_edge(node2, node, weight)                            
        
        return self.graph
    
    def _get_wight(self):
        weight = 1
        if cfg.edge_weights == 1:
                if cfg.edge_w_type == 0:
                    weight = r.randint(cfg.edge_w_interval[0], cfg.edge_w_interval[1])
                else:
                    weight = r.uniform(cfg.edge_w_interval[0], cfg.edge_w_interval[1])
        return weight
    
    def _fully_connect(self):
        
        components = []
        for node in range(self.graph.num_nodes):
            g_cmp = []
            
    def _split_to_components(self):
        pass
    

if __name__ == '__main__':
    
    gen = Graphgen()
    
    gr = gen.generate(cfg)
    print gr