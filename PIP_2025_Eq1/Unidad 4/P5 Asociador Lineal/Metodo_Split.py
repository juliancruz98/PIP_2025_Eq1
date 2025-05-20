# Asociador Lineal con validación Split

# X = Entradas
# Y = Salidas
# W = Y*XPseudoInversa

import numpy as n
import random

def verificar_balance_clases(Y):
    clases_count = {}
    total_casos = Y.shape[1]

    for i in range(Y.shape[0]):  # Para cada clase
        count = sum(Y[i])
        clases_count[i] = count

    print("\nDistribución de clases:")
    for clase, count in clases_count.items():
        print(f"Clase {clase+1}: {count} casos ({count / total_casos * 100:.2f}%)")


    valores = list(clases_count.values())
    balance = all(x == valores[0] for x in valores)

    return balance, clases_count

while True:
    try:
        porcentaje_entrenamiento = float(
            input("Ingrese el porcentaje de datos para entrenamiento (50-90): "))
        if 50 < porcentaje_entrenamiento < 100:
            break
        else:
            print("El porcentaje debe ser mayor que 50 y menor que 100.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

porcentaje_validacion = 100 - porcentaje_entrenamiento
print(f"Distribución: {porcentaje_entrenamiento:.1f}% entrenamiento, {porcentaje_validacion:.1f}% validación")

# Cargar datos
archivo = open("insdeportes.txt")
contenido = archivo.readlines()

X = contenido[3:3 + int(contenido[1])]
X = [i.split("\t") for i in X]
X = [list(map(int, i)) for i in X]

Y = contenido[3 + int(contenido[1]):]
Y = [i.split("\t") for i in Y]
Y = [list(map(int, i)) for i in Y]

X = n.array(X)
Y = n.array(Y)


total_datos = X.shape[1]
n_validacion = int(total_datos * porcentaje_validacion / 100)
n_entrenamiento = total_datos - n_validacion

print(f"\nTotal de datos: {total_datos}")
print(f"Datos para entrenamiento: {n_entrenamiento}")
print(f"Datos para validación: {n_validacion}")


hay_balance, distribucion = verificar_balance_clases(Y)
print(f"\n¿Las clases estan balanceadas? {'Sí' if hay_balance else 'No'}")

indices_por_clase = {}
for i in range(Y.shape[0]):
    indices_por_clase[i] = [j for j in range(Y.shape[1]) if Y[i][j] == 1]


indices_entrenamiento = []
indices_validacion = []

for clase, indices in indices_por_clase.items():
    random.shuffle(indices)
    n_val_clase = int(len(indices) * porcentaje_validacion / 100)

    indices_validacion.extend(indices[:n_val_clase])
    indices_entrenamiento.extend(indices[n_val_clase:])


X_entrenamiento = X[:, indices_entrenamiento]
Y_entrenamiento = Y[:, indices_entrenamiento]
X_validacion = X[:, indices_validacion]
Y_validacion = Y[:, indices_validacion]

print("\nConjunto de entrenamiento:")
hay_balance_entrenamiento, _ = verificar_balance_clases(Y_entrenamiento)
print(f"¿Conjunto de entrenamiento balanceado? {'Sí' if hay_balance_entrenamiento else 'No'}")

print("\nConjunto de validación:")
hay_balance_validacion, _ = verificar_balance_clases(Y_validacion)
print(f"¿Conjunto de validación balanceado? {'Sí' if hay_balance_validacion else 'No'}")



Paso1 = X_entrenamiento.dot(X_entrenamiento.T)
Paso2 = n.linalg.inv(Paso1)
Xpseudo = X_entrenamiento.T.dot(Paso2)
W_entrenamiento = Y_entrenamiento.dot(Xpseudo)


try:
    Paso1_val = X_validacion.dot(X_validacion.T)
    Paso2_val = n.linalg.inv(Paso1_val)
    Xpseudo_val = X_validacion.T.dot(Paso2_val)
    W_validacion = Y_validacion.dot(Xpseudo_val)
except:
    print("No se pudo calcular W para validación debido a insuficientes datos.")
    W_validacion = None

###PRUEBA DE LA FUNCIONALIDAD DEL ASOCIADOR LINEAL
# SE DECIDE PREVIAMENTE:
# 0 0 1  - VOLEIBOL
# 0 1 0  - FUTBOL
# 1 0 0  - BASQUETBOL

Clases = ["BASQUETBOL", "FUTBOL", "VOLEIBOL"]


print("\n\nEvaluacion del conjunto de entrenamiento")
casosCorrectos_entrenamiento = 0

for i in range(X_entrenamiento.shape[1]):
    casoi = X_entrenamiento[:, i]
    Ycasoi = W_entrenamiento.dot(casoi)
    Yrealcasoi = Y_entrenamiento[:, i]

    IndexMaxYcasoi = list(Ycasoi).index(max(Ycasoi))
    IndexMaxYrealcasoi = list(Yrealcasoi).index(max(Yrealcasoi))

    if IndexMaxYcasoi == IndexMaxYrealcasoi:
        casosCorrectos_entrenamiento += 1

print(f"Total de casos de entrenamiento: {X_entrenamiento.shape[1]}")
print(f"Casos correctos de entrenamiento: {casosCorrectos_entrenamiento}")
print(f"Eficiencia en entrenamiento: {casosCorrectos_entrenamiento / X_entrenamiento.shape[1] * 100.0:.2f}%")


print("\n\nEvaluacion del conjunto de validacion")
casosCorrectos_validacion = 0

for i in range(X_validacion.shape[1]):
    casoi = X_validacion[:, i]

    Ycasoi = W_entrenamiento.dot(casoi)
    Yrealcasoi = Y_validacion[:, i]

    IndexMaxYcasoi = list(Ycasoi).index(max(Ycasoi))
    IndexMaxYrealcasoi = list(Yrealcasoi).index(max(Yrealcasoi))

    if IndexMaxYcasoi == IndexMaxYrealcasoi:
        casosCorrectos_validacion += 1

print(f"Total de casos de validación: {X_validacion.shape[1]}")
print(f"Casos correctos de validación: {casosCorrectos_validacion}")
print(f"Eficiencia en validación: {casosCorrectos_validacion / X_validacion.shape[1] * 100.0:.2f}%")

# UTILIZACIÓN DEL ASOCIADOR LINEAL CON UN NUEVO CASO
print("\n\nPrueba de funcionamiento del asociador lineal con un nuevo caso: ")

#  0 0 1 Voleibol
x = [12, 45, 20, 60]
y = "VOLEIBOL"

x = n.array(x)
Ycasox = W_entrenamiento.dot(x)

print(Ycasox)
IndexMaxYcasoi = list(Ycasox).index(max(Ycasox))

print("Clase Asignada: ", Clases[IndexMaxYcasoi])
print("Correcto " if Clases[IndexMaxYcasoi] == y else "Incorrecto")