import matplotlib.pyplot as plt
import numpy as np
from Test import test

nodi = [50, 100, 150, 200, 250, 300]
percentuali = np.arange(0.0, 2.0, 0.05)  # crea vettore con elementi 0,0.05,0.10,...,1.95
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
    stringa = str(nodi[i])+" nodi nel grafo"
    legenda.append(stringa)
plt.xlabel("Percentuale di riempimento della matrice di adiacenza")
plt.ylabel("Numero di componenti fortemente connesse")
plt.legend(legenda)
plt.show()
