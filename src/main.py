from src.generator import *
from src.components.graphAM import *

gen = Graphgen()
graph = GraphAM(cfg.num_nodes, cfg.directed)


gr = gen.generate(graph, cfg)
print gr
print alg.split_to_components(gr)
gr.add_node()
gr.add_node()
print gr
print alg.split_to_components(gr)
gr.write('/home/martin/gr.amg')
