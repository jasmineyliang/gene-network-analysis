import igraph as ig
import matplotlib.pyplot as plt
import numpy as np
from igraph import power_law_fit

path = "G:\My Drive\pythonProject\COMS570HW2\graphA.txt"
listA = ig.Graph.Read_Ncol(path, names=True, directed=False)
listA.es["curved"] = False
c = listA.degree()
result = power_law_fit(c)
print(result)
#plt.hist(c)
#plt.show()


path = "G:\My Drive\pythonProject\COMS570HW2\graphB.txt"
listB = ig.Graph.Read_Ncol(path, names=True, directed=False)
listB.es["curved"] = False
c = listB.degree()
result = power_law_fit(c)
print(result)
#plt.hist(c)
#plt.show()

path = "G:\My Drive\pythonProject\COMS570HW2\graphC.txt"
listC = ig.Graph.Read_Ncol(path, names=True, directed=False)
listC.es["curved"] = False
c = listC.degree()
result = power_law_fit(c)
print(result)
#plt.hist(c)
#plt.show()

# Q6
# Base on the result from power_law_fit
# GraphA follow Power Law Distribution. (p ~= 1)
# GraphB follow Power Law Distribution. (p ~= 0.37)
# GraphC follow Power Law Distribution. (p ~= 1)

#Q7
#
# The degree distribution of all graphs follow the Power Law Distribution, which
# means they are Scale-free networks.
#
#