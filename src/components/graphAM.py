from components import Graph
from src.utiltools import mkdir
import os, sys

class GraphAM(Graph):
    
    def __init__(self, num_nodes, directed):
        Graph.__init__(self, num_nodes, directed)
        
        self.repr_type = 'AM'
        self.graph = [[0] * self.num_nodes for _ in range(self.num_nodes)]
        
    def __str__(self):
        if self.graph == None or self.graph == []:
            print "Graph not initialized"
            return
    
        str_repr = ""

        for row in self.graph:
            for col in row:
                str_repr += str(col) + " "
            str_repr += "\n"
        
        return str_repr
    
    def read(self, file_path):
        if not os.path.exists(file_path):
            sys.stderr.write('graphAM:: Error -> read : no such file exists')
            exit()
        
        self.graph = []
        with open(file_path, 'r') as fr:
            for line in fr.read().splitlines():
                if line[0] == '#':
                    continue
                self.graph.append([int(i) for i in line.split(',')])
   
    def write(self, file_path):
        mkdir(file_path)
        
        with open(file_path, 'w') as fw:
            fw.write("#Adjacency matrix graph\n")
            for row in self.graph:
                fw.write(str(row)[1:-1] + '\n')
    
    def add_node(self):
        for row in self.graph:
            row.append(0)
        self.graph.append([0] * len(self.graph[0]))
        self.num_nodes += 1
    
    def add_edge(self, start_node, end_node, value=1):
        if self.graph == None:
            print "Graph not initialized"
            return
        
        self.graph[start_node][end_node] = value
        if self.directed == 0:
            self.graph[end_node][start_node] = value
        
    def get_node_successors(self, node_idx):               
        return [index for index, succ in enumerate(self.graph[node_idx]) if succ == 1]
    
#TODO: Write unittests for graphAM.py