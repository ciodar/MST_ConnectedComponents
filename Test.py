from timeit import default_timer as timer
from Grafo import Grafo

def test(nodi, percentuali):
    tempi = []
    lunghezze = []
    pesi = []
    prove = 1
    for i in range(len(nodi)):
        tempi.append([])
        lunghezze.append([])
        pesi.append([])
        for j in percentuali:
            tempo = 0
            lung = 0
            weight = 0
            for k in range(prove):
                grafo = Grafo(nodi[i], j)
                parent,rank = grafo.union_find()
                cc = grafo.connected_components(parent)
                start = timer()
                #print(len(cc))
                res = grafo.KruskalMST()
                #grafo.KruskalMST()
                end = timer()
                tempo = tempo + (end-start)
                grafo.drawGraph()
                lung = lung + len(cc.keys())
                if res != None and len(cc.keys()) == 1:
                    for w in res:
                        weight += w[2]
            tempo = tempo / prove
            lung = lung / prove
            weight = weight / prove
            tempi[i].append(tempo)
            lunghezze[i].append(lung)
            pesi[i].append(weight)
    return tempi,lunghezze,pesi
