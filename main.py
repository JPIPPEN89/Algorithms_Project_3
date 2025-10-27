
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths.weighted import dijkstra_path
from networkx.algorithms.tree import minimum_spanning_tree

# graph one - Amanda Moore
# create the graph
unweightedG = nx.Graph()

# add the edges
unweightedG.add_edges_from([('A', 'B'), ('A', 'E'), ('A', 'F'), ('B', 'F'), ('C', 'G'),
                            ('B', 'C'), ('C', 'D'), ('D', 'G'), ('E', 'F'), ('E', 'I'),
                            ('I', 'F'), ('I', 'J'), ('I', 'M'), ('M', 'N'), ('J', 'G'),
                            ('K', 'L'), ('K', 'O'), ('L', 'P'), ('H', 'L'), ('K', 'H')])

# bfs traversal
bfs_edges = list(nx.bfs_edges(unweightedG, 'A'))
print("BFS edges:", bfs_edges,)

# dfs traversal
dfs_edges = list(nx.dfs_edges(unweightedG, 'A'))
print("DFS edges:", dfs_edges)

# find the connected components
components = list(nx.connected_components(unweightedG))
print("Connnected components:", components,"\n")

# prove a path between A and J
if (nx.has_path(unweightedG, 'A', 'J') == True):
    print("There is a path between A and J")
else:
    print("There is no path between A and J")
# prove no path between A and P
if (nx.has_path(unweightedG, 'A', 'P') == True):
    print("There is a path between A and P\n")
else:
    print("there is no path between A and P\n")

a, j = 'A', 'J'

# bfs path from two points
bfs_tree = nx.bfs_tree(unweightedG, source=a)
if j in bfs_tree:
    bfs_path = nx.shortest_path(bfs_tree, source=a, target=j)
    print(f"BFS path from {a} - {j}:", bfs_path)
else:
    print(f"BFS tree from {a} doesnt reach {j} ")

# dfs path from two points
dfs_tree = nx.dfs_tree(unweightedG, source=a)
if j in dfs_tree:
    dfs_path = nx.shortest_path(dfs_tree, source=a, target=j)
    print(f"DFS path from {a} - {j}:", dfs_path,"\n")
else:
    print(f"DFS tree from {a} does not reach {j}\n")

# end of graph 1


#graph 3
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


