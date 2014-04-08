'''
Graph mode :
    1 - adjacency list
    2 - adjacency matrix
    3 - object representation
        
Number of nodes n
        
Edge probability :
    for each two nodes is edge inserted by this probability, 1 = full graph
        
Continuous graph :
    0/1 - if 1, checks graph if all nodes are connected, if not, generates randomly new edge
        
Multigraph :
    n - if not zero, inserts n edges for every tuple of nodes, single edge with given probability
        
Directed : 0/1
'''

# --------------------
## Nodes
# --------------------

mode = 1
num_nodes = 5

# --------------------
## Edges
# --------------------

edge_prob = 0.4
cont = 0
multi_g = 0
multi_g_edge_prob = 0.1
directed = 0
loops = 0

edge_weights = 1
edge_w_type = 0             # 0 = int, 1 = float
edge_w_interval = [0, 10]

# --------------------
## Special settings
# --------------------

colored = 0
tree = 0
num_bridge = 0
num_articulations = 0
clique = 0
bipartion = 0
