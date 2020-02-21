from timeit import default_timer as timer
from Grafo import Grafo

prove_max = 100
n_prove = 50

def test(nodi, percentuali):
    tempi = []
    lunghezze = []
    pesi = []
    #Iterates using different number of nodes
    for i in range(len(nodi)):
        tempi.append([])
        lunghezze.append([])
        pesi.append([])
        #Iterates using different percentages of arc creation
        for j in percentuali:
            tempo = 0
            lung = 0
            weight = 0
            k = 0
            prove = 0
            #Does a number of tests and averages the result
            while (prove < n_prove) and (k < prove_max):
                grafo = Grafo(nodi[i], j)
                parent,rank = grafo.union_find()
                cc = grafo.connected_components(parent)
                start = timer()
                #print(len(cc))
                res = grafo.KruskalMST()
                #grafo.KruskalMST()
                end = timer()
                tempo = tempo + (end-start)
                if len(cc.keys()) == 1:
                    prove = prove + 1
                k = k+1
                #grafo.drawGraph()
                lung = lung + len(cc.keys())
                if res != None and len(cc.keys()) == 1:
                    for w in res:
                        weight += w[2]
            tempo = tempo / k
            lung = lung / k
            if prove > 0:
                weight = weight / prove
            else:
                weight = weight / k
            tempi[i].append(tempo)
            lunghezze[i].append(lung)
            pesi[i].append(weight)
    return tempi,lunghezze,pesi
