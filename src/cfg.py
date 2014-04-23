'''
Graph mode :
    1 - adjacency list
    2 - adjacency matrix
    3 - object representation
        
Number of nodes n
        
Edge probability :
    for each two nodes is edge inserted by this probability, 1 = full graph
        
Connected graph :
    0/1 - if 1, checks graph if exists path between all nodes, if not, generates randomly new edge
        
Multigraph :
    n - if not zero, inserts n edges for every tuple of nodes, single edge with given probability
        
Directed : 0/1
'''
#TODO: Write cfg description

# --------------------
## Nodes
# --------------------

num_nodes           = 7

# --------------------
## Edges
# --------------------

edge_prob           = 0.2             # 0 = every node is in separate component, 1= complete graph
full_connected      = 1             # 1 = all nodes are in single component
multi_g             = 0             # 0 = off, x = max number of multi-edges
multi_g_edge_prob   = 0.1
directed            = 1
loops               = 0

edge_weights        = 0
edge_w_type         = 0             # 0 = int, 1 = float
edge_w_interval     = [0, 10]

# --------------------
## Special settings
# --------------------

colored             = 0
tree                = 0
num_bridge          = 0
num_articulations   = 0
clique              = 0
bipartion           = 0
planar              = 0
