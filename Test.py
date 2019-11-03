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
            lung = 0
            for k in range(10):
                grafo = Grafo(nodi[i], j)
                start = timer()
                grafo.DFS()
                comp = grafo.reverse_DFS()
                end = timer()
                tempo = tempo + (end-start)
                lung = lung + comp
            tempo = tempo / 10
            lung = lung / 10
            tempi[i].append(tempo)
            lunghezze[i].append(lung)
    return [tempi, lunghezze]

