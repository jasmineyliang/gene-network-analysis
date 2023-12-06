# Q5
import igraph as ig
import numpy as np
path = "G:\My Drive\pythonProject\COMS570HW2\graphA.txt"
listA = ig.Graph.Read_Ncol(path, names=True, directed=False)
listA.es["curved"] = False
# ig.plot(listA)
#print (listA)
#d = ig._igraph.GraphBase.diameter(listA)
#print (d)

# r= ig._igraph.GraphBase.radius(listA)
# print(r)

#c = ig.Graph.transitivity_undirected(listA)
#print (c)
#ca = ig.Graph.transitivity_avglocal_undirected(listA,mode='nan')
#print (ca)

#pa = np.mean(ig._igraph.GraphBase.shortest_paths(listA))
#print (np.mean(ig._igraph.GraphBase.shortest_paths(listA)))

print(listA.vs.degree().index(listA.maxdegree()))
print(  listA.vs.betweenness().index(np.max(listA.vs.betweenness())) )


#
path = "G:\My Drive\pythonProject\COMS570HW2\graphB.txt"
listB = ig.Graph.Read_Ncol(path, names=True, directed=False)
listB.es["curved"] = False
# ig.plot(listB)
#print (listB)
#d = ig.Graph.diameter(listB)
#print (d)

# r= ig._igraph.GraphBase.radius(listB)
# print(r)

#c = ig.Graph.transitivity_undirected(listB)
#print (c)
#ca = ig.Graph.transitivity_avglocal_undirected(listB,mode='nan')
#print (ca)
#print (np.mean(ig._igraph.GraphBase.shortest_paths(listB)))
print(listB.vs.degree().index(listB.maxdegree()))
print(  listB.vs.betweenness().index(np.max(listB.vs.betweenness())) )


path = "G:\My Drive\pythonProject\COMS570HW2\graphC.txt"
listC = ig.Graph.Read_Ncol(path, names=True, directed=False)
listC.es["curved"] = False
# ig.plot(listC)
#print (listC)
#d = ig.Graph.diameter(listC)
#print (d)
# r= ig._igraph.GraphBase.radius(listC)
# print(r)
#c = ig.Graph.transitivity_undirected(listC)
#print (c)
#ca = ig.Graph.transitivity_avglocal_undirected(listC,mode='nan')
#print (ca)
#print (np.mean(ig._igraph.GraphBase.shortest_paths(listC)))
print(listC.vs.degree().index(listC.maxdegree()))
print(  listC.vs.betweenness().index(np.max(listC.vs.betweenness())) )

# (i) graphA: 100 vertices and 140 edges;
#     graphB: 100 vertices and 850 edges;
#     graphC: 200 vertices and 222 edges;
#     Hence, m~n & m<<n2, the graph is somewhere in-between dense and sparse
# (ii)
# Diameter:
#     graphA: 10;
#     graphB: 3;
#     graphC: 12;
# Radius:
#     graphA: 6;
#     graphB: 2;
#     graphC: 1;
#
# (iii)
# average clustering coefficients:
#     graphA: 0.006;
#     graphB: 0.39236190136568405;
#     graphC: 0.014166666666666664;
#
# global clustering coefficients:
#     graphA: 0.010526315789473684;
#     graphB: 0.24032730578846348;
#     graphC: 0.008021390374331552;
#
# (iV)
# average shortest path length:
#     graphA: 5.011;
#     graphB: 1.842;
#     graphC: inf;
#
# (V) using Degree Centrality and Betweenness Centrality
# MaxDegree Vertice ID in
#              GraphA: 41
#              GraphB: 43
#              GraphC: 122
# MaxBetweeness Vertice ID in
#              GraphA: 41
#              GraphB: 72
#              GraphC: 185
# Generally, we can get the same result by using different apaproaches to calculate Centrality only in the GraphA.
#
# In graphA, the node 41 has highest degree and also highest number of times acts as
# a bridge along the shortest path between two
# other nodes.
#
# In graphB, the node 43 has highest degree but node 72 has highest number of times acts as
# a bridge along the shortest path between two
# other nodes.
#
# In graphA, the node 122 has highest degree but node 185 has highest number of times acts as
# a bridge along the shortest path between two
# other nodes.
#

