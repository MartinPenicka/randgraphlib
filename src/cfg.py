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
