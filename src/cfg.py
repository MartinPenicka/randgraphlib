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

# --------------------
## Nodes
# --------------------

num_nodes           = 7

# --------------------
## Edges
# --------------------

edge_prob           = 0.3
full_connected      = 0
multi_g             = 1             # 0 = off, x = max number of multi-edges
multi_g_edge_prob   = 0.1
directed            = 0
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
