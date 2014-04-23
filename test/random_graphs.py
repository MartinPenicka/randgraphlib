from src.components.graphAM import GraphAM

class TestGraphs:
    
    def __init__(self):
        
        # Graphs for testing
        self.fully_connected = GraphAM(5)
        self.fully_separated = GraphAM(5)
        self.common_graph    = GraphAM(5)

        for x in range(5):
            for y in range(5):
                if x != y:
                    self.fully_connected.add_edge(x, y)
        
        self.common_graph.add_edge(1, 2)
        self.common_graph.add_edge(1, 3)
        self.common_graph.add_edge(2, 4)