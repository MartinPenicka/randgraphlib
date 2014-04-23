from utiltools import *
from src.utiltools import contains_same_value
from operator import concat

def BFS(graph):
    #TODO: write bfs
    pass

def split_to_components(graph):
    
    components = []
    
    def comp_cont_value(value):
        if value in [item for comp in components for item in comp]:
            return True
        return False
    
    for node in range(graph.num_nodes):
        if comp_cont_value(node):
            continue
        
        fifo = []
        fifo.append(node)
        
        tree = []
        while len(fifo) > 0:
            n = fifo.pop(0)
            tree.append(n)
            succ = graph.get_node_successors(n)
            for s in succ:
                if comp_cont_value(s):
                    tree.append(s)
                elif s not in fifo and s not in tree:
                    fifo.append(s)
        
        components.append(tree)
        
    def find_same_values(lt):
        for x in range(len(lt)):
            if x == len(lt)-1:
                break
            for y in range(x+1, len(lt)):
                if contains_same_value(lt[x], lt[y]):
                    return [x,y]
        return None
                
    while True:
        idx = find_same_values(components)
        if idx == None:
            break
        
        c1 = components.pop(idx[0])
        c2 = components.pop(idx[1]-1)
        cc = c1 + c2
        components.append(list(set(cc)))
        
    
    return components

def DFS(grpah):
    #TODO: write DFS
    pass