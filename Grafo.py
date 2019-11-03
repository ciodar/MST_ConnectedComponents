from random import random
from Nodo import Nodo

class Grafo:

    def __init__(self, n, p):
        self.m = self.createRandom(n, p)
        self.nodi = []
        for i in range(n):
            nodo = Nodo(i)
            self.nodi.append(nodo)

    def createRandom(self, n, p):
        m = []
        for i in range(n):
            m.append([])
            for j in range(n):
                r = random()
                if r <= float(p)/100:
                    m[i].append(1)
                else:
                    m[i].append(0)
        return m

    def DFS(self):
        for i in self.nodi:
            i.color = 0  # WHITE
            i.p = None
        time = 0
        for i in self.nodi:
            if i.color == 0:
                time = self.DFS_Visit(i, time)

    def DFS_Visit(self, u, time):
        time = time + 1
        u.d = time
        u.color = 1  # GRAY

        #costruisco la lista di adiacenza per il nodo u
        adj = []
        for i in range(len(self.nodi)):
            if self.m[u.id][i] == 1:
                adj.append(self.nodi[i])

        for v in adj:
            if v.color == 0:
                v.p = u
                time = self.DFS_Visit(v, time)
        u.color = 2
        time = time + 1
        u.f = time
        return time

    def reverse_DFS(self):
        self.sort()
        for i in self.nodi:
            i.color = 0
            i.p = None
        time = 0
        q = 0
        for i in self.nodi:
            if i.color == 0:
                time = self.reverse_DFS_Visit(i, time)
                q += 1
        return q

    def reverse_DFS_Visit(self, u, time):
        time = time + 1
        u.d = time
        u.color = 1

        #costruisco la lista di adiacenza per il nodo u del grafo G trasposto
        adj = []
        for i in range(len(self.nodi)):
            if self.m[i][u.id] == 1:
                for h in self.nodi:
                    if h.id == i:
                        adj.append(h)

        for v in adj:
            if v.color == 0:
                v.p = u
                time = self.reverse_DFS_Visit(v, time)
        u.color = 2
        time = time + 1
        u.f = time
        return time

    #Non utilizzato nei test, serve per vedere i nodi di ogni scc
    def SCC(self):
        self.reverse_DFS()
        self.sort()
        comp = []
        i = 0
        while i < len(self.nodi):
            discovered = self.nodi[i].d
            comp.append([])
            comp[len(comp) - 1].append(self.nodi[i])
            i = i+1
            for j in range(i,len(self.nodi)):
                if self.nodi[j].d > discovered:
                    comp[len(comp)-1].append(self.nodi[j])
                    i = i+1
        return comp

    #ordina in modo decrescente i nodi in base al loro tempo di completamento di visita
    def sort(self):
        self.nodi.sort(key=lambda x: x.f, reverse=True)



