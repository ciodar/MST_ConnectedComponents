import matplotlib.pyplot as plt
import numpy as np

from Test import test
percentuali = list()
nodi = [10, 20, 30, 40, 50, 60]
percentuali = np.arange(0.0,0.5,0.05)  # crea vettore con elementi 0,0.05,0.10,...,1.95
t = test(nodi, percentuali)

#Creo i grafici

plt.figure(1)
legenda = []
for i in range(len(t[0])):
    plt.plot(percentuali, t[0][i])
    stringa = str(nodi[i]) + " nodi nel grafo"
    legenda.append(stringa)
plt.xlabel("Percentuale di riempimento della matrice di adiacenza")
plt.ylabel("Tempo impiegato")
plt.legend(legenda)

plt.figure(2)
legenda = []
for i in range(len(t[1])):
    plt.plot(percentuali, t[1][i])
    stringa = str(nodi[i]) + " nodi nel grafo"
    legenda.append(stringa)
plt.xlabel("Percentuale di riempimento della matrice di adiacenza")
plt.ylabel("Numero di componenti connesse")
plt.legend(legenda)

plt.figure(3)
legenda = []
for i in range(len(t[2])):
    plt.plot(percentuali, t[2][i])
    stringa = str(nodi[i]) + " nodi nel grafo"
    legenda.append(stringa)
plt.xlabel("Percentuale di riempimento della matrice di adiacenza")
plt.ylabel("Peso totale del grafo")
plt.legend(legenda)
plt.show()
