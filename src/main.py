from src.generator import Graphgen
from src.components.graphAM import GraphAM
from src.components.graphNodes import GraphNodes
import algorithms as alg
import cfg as cfg

gen = Graphgen()
#graph = GraphAM(cfg.num_nodes, cfg.directed)
graph = GraphNodes(cfg.num_nodes, cfg.directed)

gr = gen.generate(graph, cfg)

gr.plot_to_file('/home/martin/pokus.png')

#alg.max_pairing(gr)
