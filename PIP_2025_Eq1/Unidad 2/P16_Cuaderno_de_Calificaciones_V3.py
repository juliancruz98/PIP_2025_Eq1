archivo = open( "../Archivos/calificaciones_con_nombre.csv")
contenido = archivo.readlines()

datos = [i.split(",") for i in contenido]

datos = [[i[0],list(map(int, i[1:]))]for i in datos]


datos = [[i[0],i[1], sum(i[1])/len(i[1])] for i in datos]
print(datos)



nombres = [i[0] for i in datos]
promedios = [i[2] for i in datos]

promGroup = sum(promedios)/len(promedios)

import numpy as np
vector = np.array(promedios)
desviacion = np.std(vector)

print("Promedio Grupo:", promGroup)
print("Desviacion Grupo:", desviacion)

promedios_std = [(i-promGroup)/desviacion for i in promedios]

referencias = [0 for i in range(len(promedios))]

from matplotlib import pyplot as plt
plt.plot(nombres, promedios_std, linestyle='-')
plt.plot(nombres, referencias, color='red', marker='o')
plt.grid(True)
plt.show()