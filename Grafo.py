import random
from Nodo import Nodo
import networkx as nx
import matplotlib.pyplot as plt
WEIGHT_MIN = 1
WEIGHT_MAX = 10

class Grafo:

    def __init__(self, n, p):
        self.nodi,self.m = self.createRandom(n, p)
    #def __init__(self):
    #    self.nodi = set()
    #    self.m = set()

    # POST: creates a random connected graph with a V-1 edges
    def createRandom(self, n, p):
        nodi = set()
        m = dict()
        for i in range(n):
            nodo = Nodo(i)
            nodi.add(nodo)
            for j in range(n):
                r = random.random()
                if r <= float(p)/100:
                    w = random.randint(WEIGHT_MIN, WEIGHT_MAX)
                    edge = (j,w)
                    edge2 = (i,w)
                    if i not in m.keys():
                        m[i] = set()
                    m[i].add(edge)
                    if j not in m.keys():
                        m[j] = set()
                    m[j].add(edge2)
        return nodi,m

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

        #ordina in modo decrescente i nodi in base al loro tempo di completamento di visita
    def sort(self):
        self.nodi.sort(key=lambda x: x.f, reverse=True)

    def archi_sort(self):
        self.m = sorted(self.m, key=lambda item: item[2])

    def get_all_connected_groups(self):
        already_seen = set()
        result = []
        for node in grafo.m.keys():
            if node not in already_seen:
                connected_group, already_seen = self.get_connected_group(node, already_seen)
                result.append(connected_group)
        return result

    def get_connected_group(self,node, already_seen):
        result = []
        nodes = set([node])
        while nodes:
            node = nodes.pop()
            already_seen.add(node)
            nodes = nodes or {v[0] for v in grafo.m[node]} - already_seen
            result.append(node)
        return result, already_seen


if __name__ == '__main__':
    print("creating new grafo")
    G = nx.Graph()
    grafo = Grafo(20,5)
    G.add_nodes_from(map(lambda Nodo: Nodo.id, grafo.nodi))
    for k, v in grafo.m.items():
        for vv in v:
            G.add_edge(k,vv[0])
    #grafo.nodi = (0, 1, 2, 3, 4)
    #edge = (1, 0, 1)
    #grafo.m.add(edge)
    #edge = (2, 3, 1)
    #grafo.m.add(edge)
    #edge = (3, 4, 1)
    #grafo.m.add(edge)
    cc = grafo.get_all_connected_groups()
    for nodo in cc:
        print(nodo)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()