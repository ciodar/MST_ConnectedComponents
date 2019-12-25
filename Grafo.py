import random
import networkx as nx
import matplotlib.pyplot as plt
WEIGHT_MIN = 1
WEIGHT_MAX = 100

class Grafo:

    def __init__(self, n, p):
        self.m = self.createRandom(n, p)
    #def __init__(self):
    #    self.nodi = set()
    #    self.m = set()

    # POST: creates a random connected graph with a V-1 edges
    def createRandom(self, n, p):
        m = dict()
        for i in range(n):
            if i not in m.keys():
                m[i] = set()
            for j in range(n):
                if i != j:
                    r = random.random()
                    if r <= float(p):
                        w = random.randint(WEIGHT_MIN, WEIGHT_MAX)
                        edge = (j,w)
                        edge2 = (i,w)
                        m[i].add(edge)
                        if j not in m.keys():
                            m[j] = set()
                        m[j].add(edge2)
        return m

    def edge_sort(self):
        edges = list()
        for k, v in self.m.items():
            for vv in v:
                edges.append((k, vv[0],vv[1]))
        edges = sorted(edges, key=lambda item: item[2])
        return edges

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

            # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def get_all_connected_groups(self):
        already_seen = set()
        result = []
        for node in self.m.keys():
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
            for n in {v[0] for v in self.m[node]} - already_seen - nodes:
                nodes.add(n)
            result.append(node)
        return result, already_seen
    def draw(self,G):

        esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 3]
        enormal = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 3 and d['weight'] <= 5]
        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 5 and d['weight'] <= 7]
        exlarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 7]
        # nx.draw(G, with_labels=True, font_weight='bold')
        pos = nx.circular_layout(G)  # positions for all nodes
        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=500)
        # edges
        nx.draw_networkx_edges(G, pos, edgelist=esmall, width=1, edge_color='b', style='dashed')
        nx.draw_networkx_edges(G, pos, edgelist=enormal, width=1, edge_color='g')
        nx.draw_networkx_edges(G, pos, edgelist=elarge, width=1, edge_color='y')
        nx.draw_networkx_edges(G, pos, edgelist=exlarge, width=1, edge_color='r')
        # labels
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
        plt.show()

    def drawGraph(self):
        G = nx.Graph()
        G.add_nodes_from(self.m.keys())
        for k, v in self.m.items():
            for vv in v:
                G.add_edge(k, vv[0], weight=vv[1])
        esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 3]
        enormal = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 3 and d['weight'] <= 5]
        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 5 and d['weight'] <= 7]
        exlarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 7]
        # nx.draw(G, with_labels=True, font_weight='bold')
        pos = nx.circular_layout(G)  # positions for all nodes
        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=500)
        # edges
        nx.draw_networkx_edges(G, pos, edgelist=esmall, width=1, edge_color='b', style='dashed')
        nx.draw_networkx_edges(G, pos, edgelist=enormal, width=1, edge_color='g')
        nx.draw_networkx_edges(G, pos, edgelist=elarge, width=1, edge_color='y')
        nx.draw_networkx_edges(G, pos, edgelist=exlarge, width=1, edge_color='r')
        # labels
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
        plt.show()

    def KruskalMST(self):

        result = []  # This will store the resultant MST

        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]

        # Step 1:  Sort all the edges in non-decreasing
        # order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        edges = self.edge_sort()

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(len(self.m.keys())):
            parent.append(node)
            rank.append(0)
        if len(edges) < len(self.m.keys()) - 1:
            #print("Given graph can't be connected")
            return
            # Number of edges to be taken is equal to V-1
        while e < len(self.m.keys()) - 1 and i < len(edges):

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, weight = edges[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't cause cycle,
            # include it in result and increment the index
            # of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, weight])
                self.union(parent, rank, x, y)
                # Else discard the edge
        H = nx.Graph()
        H.add_nodes_from(self.m.keys())
        # print the contents of result[] to display the built MST
        if(e < len(self.m.keys()) -1):
            print("Cannot build MST for this graph. The graph is not connected")

        return result
        #print("Following are the edges in the constructed MST")
        #for u, v, weight in result:

        #    H.add_edge(u,v,weight=weight)
            # print str(u) + " -- " + str(v) + " == " + str(weight)
        #    print("%d -- %d == %d" % (u, v, weight))
        #self.draw(H)
if __name__ == '__main__':
    print("creating new grafo")

    grafo = Grafo(20,10)
    G = nx.Graph()
    G.add_nodes_from(grafo.m.keys())
    for k, v in grafo.m.items():
        for vv in v:
            G.add_edge(k, vv[0], weight=vv[1])
    grafo.draw(G)

    cc = grafo.get_all_connected_groups()
    print(cc)
    edges = grafo.edge_sort()
    print(edges)
    grafo.KruskalMST()