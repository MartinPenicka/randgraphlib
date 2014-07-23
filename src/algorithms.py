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

def max_pairing(graph):
    '''
    In this time works only with GraphNode
    '''
    
    free_nodes = []
    
    def reset_values():
        for node in graph.graph:
            node.link = None
            node.first = None
            
    def get_edge(node_v):
        
        if node_v.link == None:
            return False
        
        for node in node_v.neighbours:
            if node.link == None and node.first == None:
                return node
            
        return False
    
    def add_free_node_to_pairing(v, w):
        
        while True:
            v_mate = v.mate
            v_link = v.link
            
            w.mate = v
            v.mate = w
            
            v = v_link
            w = v_mate
            if v == 0:
                return
            
            if v.link == 0:
                return
            
    def print_pairing():
        for node in graph.graph:
            print node.mate.idx
            
    def find_path(fn):
        
        if len(fn.neighbours) == 0:
            return
        
        reset_values()
        fn.link = 0
        fn.first = 0
        
        v = fn
        
        while True:
            w = get_edge(v)
            if w == False:
                return
            elif w.mate == None:
                add_free_node_to_pairing(v, w)
            else:
                if w.link != None:
                    z = w.mate
                    z.link = v
                    z.first = w
                    v = z
                    continue
                elif v.first == w.first:
                    continue
                else:
                    r = v.first
                    S = [r]
                    while r != 0:
                        r = ((r.mate).link).first
                        S.append(r)
                        
                    r = w.first
                    while r not in S:
                        r = ((r.mate).link).first
                    JOIN = r
                    
                    r = v.first
                    while r != JOIN:
                        r.link = [v, w]
                        r.first = JOIN
                        r = ((r.mate).link).first
                        
                    r = w.first
                    while r != JOIN:
                        r.link = [v, w]
                        r.first = JOIN
                        r = ((r.mate).link).first
                        
                    for node in graph.graph:
                        if node.link != None and (node.first).link != None:
                            node.first = JOIN
                    continue
                    
    for node in graph.graph:
        node.mate = None
        reset_values()
        
        free_nodes.append(node)
        
    while len(free_nodes) != 0:
        
        f_n = free_nodes.pop()
        find_path(f_n)
        
    print_pairing()
    
    