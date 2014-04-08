
import components as cmpn
import random as r
import cfg

class Graphgen:
    
    def __init__(self):
        pass
    
    def generate(self, cfg):
        
        graph = cmpn.Graph(cfg.num_nodes, cfg.mode)
        
        for node in range(graph.node_num):
            for node2 in range(graph.node_num):
                if node == node2 and cfg.loops == 0:
                    continue
                
                # add new edge
                if r.random() < cfg.edge_prob:
                    
                    weight = self._get_wight()
                    
                    graph.add_edge(node, node2, weight)
                    if cfg.directed == 0:
                        graph.add_edge(node2, node, weight)
                    
                    if cfg.multi_g > 0 and graph.mode != 1:
                        for _ in range(cfg.multi_g):
                            if r.random() < cfg.multi_g_edge_prob:
                                weight = self._get_wight()
                                
                                graph.add_edge(node, node2, weight)
                                if cfg.directed == 0:
                                    graph.add_edge(node2, node, weight)                            
        
        return graph
    
    def _get_wight(self):
        weight = 1
        if cfg.edge_weights == 1:
                if cfg.edge_w_type == 0:
                    weight = r.randint(cfg.edge_w_interval[0], cfg.edge_w_interval[1])
                else:
                    pass
        return weight
    
    def aa(self):
        pass
    

if __name__ == '__main__':
    
    gen = Graphgen()
    
    gr = gen.generate(cfg)
    print gr