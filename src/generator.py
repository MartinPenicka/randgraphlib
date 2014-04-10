
from components import graphAM as g
import random as r
import cfg
import cfg_tester
import algorithms as alg

class Graphgen:
    
    def __init__(self):
        self.graph = None
    
    def set_graph(self, graph):
        self.graph = graph
    
    def generate(self, cfg):
        
        self.cfg = cfg
        cfg_tester.test_cfg_file(cfg)
        
        #TODO: graph module must not depend on representation
        if self.graph == None:
            self.graph = g.GraphAM(cfg.num_nodes)
        
        for node in range(self.graph.num_nodes):
            for node2 in range(self.graph.num_nodes):
                if node == node2 and cfg.loops == 0:
                    continue
                
                # add new edge
                if r.random() < cfg.edge_prob:
                    
                    #TODO: repair get weight -> not same in common graph
                    self.graph.add_edge(node, node2, self._get_weight())
                    if cfg.directed == 0:
                        self.graph.add_edge(node2, node, self._get_weight())
                    
                    if cfg.multi_g > 0 and self.graph.repr_type != 'AM':
                        for _ in range(cfg.multi_g):
                            if r.random() < cfg.multi_g_edge_prob:                                
                                self.graph.add_edge(node, node2, self._get_weight())
                                if cfg.directed == 0:
                                    self.graph.add_edge(node2, node, self._get_weight())
        if cfg.full_connected == 1:
            self._fully_connect()                        
        
        return self.graph
    
    def _get_weight(self):
        weight = 1
        if cfg.edge_weights == 1:
                if cfg.edge_w_type == 0:
                    weight = r.randint(cfg.edge_w_interval[0], cfg.edge_w_interval[1])
                else:
                    weight = r.uniform(cfg.edge_w_interval[0], cfg.edge_w_interval[1])
        return weight
    
    def _fully_connect(self):
        
        components = alg.split_to_components(self.graph)
        while len(components) != 1:
            c1 = components.pop(0)
            c2 = components.pop(0)
            
            n1 = r.randint(0, len(c1)-1)
            n2 = r.randint(0, len(c2)-1)
            self.graph.add_edge(c1[n1], c2[n2], self._get_weight())
            if self.cfg.directed == 0:
                self.graph.add_edge(c1[n2], c2[n1], self._get_weight())
            
            new_c = c1 + c2
            components.append(new_c)
            print len(components)
        print len(components)
        print components
            
    

if __name__ == '__main__':
    
    gen = Graphgen()
    
    gr = gen.generate(cfg)
    print gr
    print alg.split_to_components(gr)