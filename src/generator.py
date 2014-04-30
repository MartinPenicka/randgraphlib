
from components.graphAM import GraphAM
import random as r
import cfg
import cfg_tester
import algorithms as alg

class Graphgen:
    
    def __init__(self):
        pass
    
    def generate(self, graph, cfg):
        
        if not cfg_tester.test_cfg_file(cfg):
            exit(1)
        
        self.gen_simple_graph(graph, cfg)

        if cfg.full_connected == 1:
            self.fully_connect(graph)                        
        
        return graph
    
    def _get_weight(self):
        weight = 1
        if cfg.edge_weights == 1:
                if cfg.edge_w_type == 0:
                    weight = r.randint(cfg.edge_w_interval[0], cfg.edge_w_interval[1])
                else:
                    weight = r.uniform(cfg.edge_w_interval[0], cfg.edge_w_interval[1])
        return weight
    
    def gen_simple_graph(self, graph, cfg):
        for node in range(graph.num_nodes):
            for node2 in range(graph.num_nodes):
                if node == node2 and cfg.loops == 0:
                    continue
                
                # add new edge
                if r.random() < cfg.edge_prob:
                    
                    graph.add_edge(node, node2, self._get_weight())
                    
                    if cfg.multi_g > 0 and graph.repr_type != 'AM':
                        for _ in range(cfg.multi_g):
                            if r.random() < cfg.multi_g_edge_prob:                                
                                graph.add_edge(node, node2, self._get_weight())
    
    def fully_connect(self, graph):
        
        components = alg.split_to_components(graph)
        while len(components) > 1:
            c1 = components.pop(0)
            c2 = components.pop(0)
            
            n1 = r.randint(0, len(c1)-1)
            n2 = r.randint(0, len(c2)-1)
            graph.add_edge(c1[n1], c2[n2], self._get_weight())
            
            new_c = c1 + c2
            components.append(new_c)
