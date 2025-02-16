archivo = open( "../Archivos/calificaciones_con_nombre.csv")
contenido = archivo.readlines()

print(contenido)

datos = [i.split(",") for i in contenido]

print(datos)


datos = [[i[0],list(map(int, i[1:]))]for i in datos]

print(datos)

#investigar como calcular el promedio de cada alumno y agregar el resultado a la lista asociada al usuario

datos = [[i[0],i[1], sum(i[1])/len(i[1])] for i in datos]
print(datos)

#Investigar como graficar valores de ese estilo (calificaciones) y ya después cómo hacerla en python
#habia que sacar un histograma 12/02/2025
datos.sort(key=lambda x:x[1])

nombres = [i[0] for i in datos]
promedios = [i[2] for i in datos]

promGroup = sum(promedios)/len(promedios)
promGroup = [promGroup for i in range(len(promedios))]
print(promGroup)



from matplotlib import pyplot as plt

plt.plot(nombres, promedios, marker='x', color='red')
plt.plot(nombres, promGroup, marker='o', color='purple')
plt.bar(nombres, promedios)

plt.title('Resumen de calif')
plt.xlabel('Nombres')
plt.ylabel('Promedios')
plt.ylim(0,12)

plt.show()

