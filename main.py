
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths.weighted import dijkstra_path
from networkx.algorithms.tree import minimum_spanning_tree

und_weight_g = nx.Graph()

# Building undirected weighted graph
und_weight_g.add_edge('A','B', weight=22)
und_weight_g.add_edge('A','C', weight=9)
und_weight_g.add_edge('A','D', weight=12)

und_weight_g.add_edge('B','C', weight=35)
und_weight_g.add_edge('B','F', weight=36)
und_weight_g.add_edge('B','H', weight=34)

und_weight_g.add_edge('C','D', weight=4)
und_weight_g.add_edge('C','E', weight=65)
und_weight_g.add_edge('C','F', weight=42)

und_weight_g.add_edge('D','E', weight=33)
und_weight_g.add_edge('D','I', weight=30)

und_weight_g.add_edge('E','F', weight=18)
und_weight_g.add_edge('E','G', weight=23)

und_weight_g.add_edge('F','H', weight=24)
und_weight_g.add_edge('F','G', weight=39)

und_weight_g.add_edge('G','I', weight=21)
und_weight_g.add_edge('G','H', weight=25)
und_weight_g.add_edge('H','I', weight=19)

# Question 3(a)
# Running Dijkstra's algorithm, saving distance and paths took
dist, paths = nx.single_source_dijkstra(und_weight_g, source='A', weight='weight')

for key, val in dist.items():
    print(f'dist(A,{key}) = {val}')

print('Paths are hand drawn in the report.\n')

# Question 3(b)
# Using Kruskal's algorithm for minimum spanning tree
mst = nx.minimum_spanning_tree(und_weight_g, weight='weight', algorithm='kruskal')

# List MST edges with weights
print(list(mst.edges(data=True)))

# Total weight of the MST
total = sum(d['weight'] for _, _, d in mst.edges(data=True))
print("Total MST weight:", total)

# Number of edges
print("Edges in MST:", mst.number_of_edges(), '\n')

#Question 3(c)
spt_edges = set()
for v, path in paths.items():
    if len(path) > 1:
        u = path[-2]
        spt_edges.add(tuple(sorted((u, v))))

mst_edges = {tuple(sorted((u, v))) for u, v in mst.edges()}
print("SPT edges:", spt_edges)
print("MST edges:", mst_edges)
print("Are MST and SPT Equal?", spt_edges == mst_edges, '\n')

#Question 3(d)
# Creating graph with negative weights
neg_graph = und_weight_g.copy()
neg_graph.add_edge('C','A', weight=-20)


# Setting a try and except b/c dijkstras algorithm should fail with negative weights
try:
    dist, paths = nx.single_source_dijkstra(neg_graph, source='A', weight='weight')
    print(dist)
    print(paths)

except:
    print('Djikstras Algorithm does not work with negative weights')