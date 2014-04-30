'''
Test config file for parameters inconsistency
(example : tree & clique > 2 -> such graph does not exist)
'''

def test_cfg_file(cfg):
    
    errors = 0
    
    def ae():       # add error
        # increase number of found errors
        errors += 1
    
    if cfg.edge_prob == 0 and cfg.full_connected:
        print("ERROR: cfg consistency : Graph cannot be full connected with zero edges.")
        ae()
        
    if cfg.tree == 1 and cfg.clique >=3:
        print("ERROR: cfg consistency : Graph cannot be tree and containd clique bigger than 2.")
        ae()
        
    if cfg.planar == 1 and cfg.clique >= 5:
        print("ERROR: cfg consistency : Planar graph cannot have clique >= 5.")
        ae()
        
        
    # last if, check if cfg file containd inconsistency
    if errors > 0:
        print "Found " + str(errors)
        return False
    
    return True