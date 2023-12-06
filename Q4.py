import igraph as ig
print(ig.__version__)
from igraph import *
g = Graph()
g.add_vertices(5)
g.add_edges([(0, 1),(0, 2),(0, 4) ,(0, 3), (1, 3), (1, 4), (2, 4), (4,3),(2,3),(2,1)])
print(g)
ig.plot(g)
