
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths.weighted import dijkstra_path
from networkx.algorithms.tree import minimum_spanning_tree

und_weight_g = nx.Graph()

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

dist, paths = nx.single_source_dijkstra(und_weight_g, source='A', weight='weight')

for key, val in dist.items():
    print(f'dist(A,{key}) = {val}')

print('Paths are hand drawn in the report.\n')

mst = nx.minimum_spanning_tree(und_weight_g, weight='weight', algorithm='kruskal')

# List MST edges with weights
print(list(mst.edges(data=True)))

# Total weight of the MST
total = sum(d['weight'] for _, _, d in mst.edges(data=True))
print("Total MST weight:", total)

# Number of edges (should be len(G) - 1 if connected)
print("Edges in MST:", mst.number_of_edges())


