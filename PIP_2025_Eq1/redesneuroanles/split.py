# Asociador Lineal con Validación Split

import numpy as np
import random


# Función para cargar los datos
def cargar_datos(archivo_nombre):
    archivo = open(archivo_nombre)
    contenido = archivo.readlines()

    X = contenido[3:3 + int(contenido[1])]
    X = [i.split("\t") for i in X]
    X = [list(map(int, i)) for i in X]

    Y = contenido[3 + int(contenido[1]):]
    Y = [i.split("\t") for i in Y]
    Y = [list(map(int, i)) for i in Y]

    # Convertir a numpy array
    X = np.array(X)
    Y = np.array(Y)

    # Verificar y ajustar la orientación de la matriz si es necesario
    if X.shape[0] > X.shape[1]:
        print("Transponiendo la matriz X para tener características como filas y ejemplos como columnas")
        X = X.T

    if Y.shape[0] > Y.shape[1]:
        print("Transponiendo la matriz Y para tener clases como filas y ejemplos como columnas")
        Y = Y.T

    return X, Y


# Función para calcular la matriz W
def calcular_W(X, Y):
    Paso1 = X.dot(X.T)
    Paso2 = np.linalg.inv(Paso1)
    Xpseudo = X.T.dot(Paso2)
    W = Y.dot(Xpseudo)
    return W


# Función para evaluar el desempeño del asociador
def evaluar_asociador(X, Y, W, Clases):
    casosCorrectos = 0

    for i in range(X.shape[1]):
        casoi = X[:, i]
        Ycasoi = W.dot(casoi)
        Yrealcasoi = Y[:, i]

        IndexMaxYcasoi = list(Ycasoi).index(max(Ycasoi))
        IndexMaxYrealcasoi = list(Yrealcasoi).index(max(Yrealcasoi))

        if IndexMaxYcasoi == IndexMaxYrealcasoi:
            casosCorrectos += 1

    eficiencia = casosCorrectos / X.shape[1] * 100.0 if X.shape[1] > 0 else 0
    return casosCorrectos, eficiencia


# Función para verificar balance de clases
def verificar_balance_clases(Y):
    num_clases = Y.shape[0]
    num_ejemplos = Y.shape[1]

    conteo_clases = [0] * num_clases
    for i in range(num_ejemplos):
        for j in range(num_clases):
            if Y[j][i] == 1:
                conteo_clases[j] += 1
                break

    # Verificar si las clases están balanceadas
    balanceado = all(x == conteo_clases[0] for x in conteo_clases)

    return balanceado, conteo_clases


# Función para dividir los datos en entrenamiento y validación
def dividir_datos(X, Y, porcentaje_entrenamiento):
    num_ejemplos = X.shape[1]
    num_entrenamiento = int(num_ejemplos * porcentaje_entrenamiento / 100)
    num_validacion = num_ejemplos - num_entrenamiento

    # Obtener índices de cada clase
    num_clases = Y.shape[0]
    indices_por_clase = [[] for _ in range(num_clases)]

    for i in range(num_ejemplos):
        for j in range(num_clases):
            if Y[j][i] == 1:
                indices_por_clase[j].append(i)
                break

    # Dividir índices por clase
    indices_entrenamiento = []
    indices_validacion = []

    for indices_clase in indices_por_clase:
        num_clase = len(indices_clase)
        num_entrenamiento_clase = int(num_clase * porcentaje_entrenamiento / 100)

        # Mezclar índices
        random.shuffle(indices_clase)

        # Dividir
        indices_entrenamiento.extend(indices_clase[:num_entrenamiento_clase])
        indices_validacion.extend(indices_clase[num_entrenamiento_clase:])

    # Crear matrices de entrenamiento y validación
    X_entrenamiento = X[:, indices_entrenamiento]
    Y_entrenamiento = Y[:, indices_entrenamiento]

    X_validacion = X[:, indices_validacion]
    Y_validacion = Y[:, indices_validacion]

    return X_entrenamiento, Y_entrenamiento, X_validacion, Y_validacion


# Configuración inicial
archivo_nombre = "insdeportes.txt"
Clases = ["REGULAR", "MALO", "BUENO"]

# Cargar los datos
X, Y = cargar_datos(archivo_nombre)


# Verificar balance de clases
balanceado, conteo_clases = verificar_balance_clases(Y)
print("\nVerificación de balance de clases:")
print("¿Clases balanceadas?:", "Sí" if balanceado else "No")
print("Distribución de clases:")
for i, clase in enumerate(Clases):
    print(f"  {clase}: {conteo_clases[i]} ejemplos")

# Solicitar porcentaje de validación al usuario
while True:
    try:
        porcentaje_entrenamiento = float(
            input("\nIngrese el porcentaje para entrenamiento (mayor que 50 y menor que 100): "))
        if 50 < porcentaje_entrenamiento < 100:
            break
        else:
            print("El porcentaje debe ser mayor que 50 y menor que 100.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

porcentaje_validacion = 100 - porcentaje_entrenamiento

# Calcular cantidad de datos para entrenamiento y validación
num_total = X.shape[1]
num_entrenamiento = int(num_total * porcentaje_entrenamiento / 100)
num_validacion = num_total - num_entrenamiento

print(f"\nDivisión de datos:")
print(f"  Total: {num_total} ejemplos")
print(f"  Entrenamiento ({porcentaje_entrenamiento}%): {num_entrenamiento} ejemplos")
print(f"  Validación ({porcentaje_validacion}%): {num_validacion} ejemplos")

# Dividir los datos
X_entrenamiento, Y_entrenamiento, X_validacion, Y_validacion = dividir_datos(X, Y, porcentaje_entrenamiento)

print("\nDimensiones después de la división:")
print(f"  X_entrenamiento: {X_entrenamiento.shape}")
print(f"  Y_entrenamiento: {Y_entrenamiento.shape}")
print(f"  X_validacion: {X_validacion.shape}")
print(f"  Y_validacion: {Y_validacion.shape}")

# Verificar balance en los conjuntos separados
balance_entrenamiento, conteo_entrenamiento = verificar_balance_clases(Y_entrenamiento)
balance_validacion, conteo_validacion = verificar_balance_clases(Y_validacion)

print("\nBalance en conjunto de entrenamiento:")
print("¿Clases balanceadas?:", "Sí" if balance_entrenamiento else "No")
print("Distribución de clases en entrenamiento:")
for i, clase in enumerate(Clases):
    print(f"  {clase}: {conteo_entrenamiento[i]} ejemplos")

print("\nBalance en conjunto de validación:")
print("¿Clases balanceadas?:", "Sí" if balance_validacion else "No")
print("Distribución de clases en validación:")
for i, clase in enumerate(Clases):
    print(f"  {clase}: {conteo_validacion[i]} ejemplos")

# Calcular W para entrenamiento
W_entrenamiento = calcular_W(X_entrenamiento, Y_entrenamiento)
print("\nMatriz W (entrenamiento):")
print(W_entrenamiento)

# Calcular W para validación (si hay suficientes datos)
if X_validacion.shape[1] > 0:
    try:
        W_validacion = calcular_W(X_validacion, Y_validacion)
        print("\nMatriz W (validación):")
        print(W_validacion)
    except np.linalg.LinAlgError:
        print("\nNo se puede calcular W para validación (matriz singular)")
        W_validacion = None
else:
    print("\nNo hay suficientes datos para calcular W de validación")
    W_validacion = None

# Evaluar en conjunto de entrenamiento
print("\n--- EVALUACIÓN EN CONJUNTO DE ENTRENAMIENTO ---")
casos_correctos_entrenamiento, eficiencia_entrenamiento = evaluar_asociador(X_entrenamiento, Y_entrenamiento,
                                                                            W_entrenamiento, Clases)

print(f"Total de casos de entrenamiento: {X_entrenamiento.shape[1]}")
print(f"Casos correctos en entrenamiento: {casos_correctos_entrenamiento}")
print(f"Eficiencia en entrenamiento: {eficiencia_entrenamiento:.2f}%")

# Evaluar en conjunto de validación
if X_validacion.shape[1] > 0:
    print("\n--- EVALUACIÓN EN CONJUNTO DE VALIDACIÓN ---")
    casos_correctos_validacion, eficiencia_validacion = evaluar_asociador(X_validacion, Y_validacion, W_entrenamiento,
                                                                          Clases)

    print(f"Total de casos de validación: {X_validacion.shape[1]}")
    print(f"Casos correctos en validación: {casos_correctos_validacion}")
    print(f"Eficiencia en validación: {eficiencia_validacion:.2f}%")

# Prueba de funcionamiento con un nuevo caso
print("\n\nPrueba de funcionamiento del asociador lineal entrenado:")
x = np.array([78, 53, 11, 30, 86, 23])
y_esperado = "BUENO"

# Verificar dimensiones para compatibilidad
print(f"Dimensiones de W_entrenamiento: {W_entrenamiento.shape}")
print(f"Dimensiones de vector x: {x.shape}")

# Verificar si necesitamos ajustar las dimensiones
if W_entrenamiento.shape[1] != len(x):
    print(f"ADVERTENCIA: Las dimensiones no son compatibles.")
    print(f"El vector de prueba debería tener {W_entrenamiento.shape[1]} elementos para ser compatible con W.")
    # Ajustar x si es posible (recortar o rellenar según sea necesario)
    if len(x) > W_entrenamiento.shape[1]:
        print(f"Recortando el vector de prueba a los primeros {W_entrenamiento.shape[1]} elementos...")
        x = x[:W_entrenamiento.shape[1]]
    else:
        print(f"El vector de prueba es demasiado corto y no se puede adaptar automáticamente.")
        print("Por favor, ajusta el vector de prueba manualmente.")
        # Aquí podrías implementar lógica para rellenar x si es necesario

try:
    Ycasox = W_entrenamiento.dot(x)
    print("Salidas generadas:")
    print(Ycasox)

    IndexMaxYcasoi = list(Ycasox).index(max(Ycasox))
    print(f"Clase Asignada: {Clases[IndexMaxYcasoi]}")
    print("Correcto " if Clases[IndexMaxYcasoi] == y_esperado else "Incorrecto")
except ValueError as e:
    print(f"Error al calcular la salida: {e}")
    print("No se puede realizar la predicción debido a incompatibilidad de dimensiones.")