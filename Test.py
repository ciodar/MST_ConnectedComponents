from timeit import default_timer as timer
from Grafo import Grafo

def test(nodi, percentuali):
    tempi = []
    lunghezze = []
    for i in range(len(nodi)):
        tempi.append([])
        lunghezze.append([])
        for j in percentuali:
            tempo = 0
            for k in range(10):
                grafo = Grafo(nodi[i], j)
                start = timer()
                cc = grafo.connectedComponents()
                print("Connected components are:")
                for nodo in cc:
                    print(nodo)
                #grafo.KruskalMST()
                end = timer()
                tempo = tempo + (end-start)
            tempo = tempo / 10
            tempi[i].append(tempo)
    return tempi
