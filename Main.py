import matplotlib.pyplot as plt
import numpy as np

from Test import test

G = nx.Graph()
nodi = [50, 100, 150, 200, 250, 300]
percentuali = np.arange(0.0, 2.0, 0.05)  # crea vettore con elementi 0,0.05,0.10,...,1.95
#t = test(nodi, percentuali)
for line in nx.generate_adjlist(G):
    print(line)
# write edgelist to grid.edgelist
nx.write_edgelist(G, path="grid.edgelist", delimiter=":")
# read edgelist from grid.edgelist
H = nx.read_edgelist(path="grid.edgelist", delimiter=":")

nx.draw(H)
#Creo i grafici

#plt.figure(1)
#legenda = []

plt.show()
