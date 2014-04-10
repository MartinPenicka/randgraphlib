from utiltools import *

def BFS(graph):
    #TODO: write bfs
    pass

def split_to_components(graph):
    
    components = []
    for node in range(graph.num_nodes):
        if recursive_contains(components, node):
            continue
        
        fifo = []
        fifo.append(node)
        
        tree = []
        while len(fifo) > 0:
            n = fifo.pop(0)
            tree.append(n)
            succ = graph.get_node_successors(n)
            for s in succ:
                if s not in fifo and s not in tree:
                    fifo.append(s)
        
        components.append(tree)
    
    return components

def DFS(grpah):
    #TOSO: write DFS
    pass