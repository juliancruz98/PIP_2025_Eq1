import numpy as n

# Leer archivo y procesar datos
archivo = open("insdeportes.txt")
contenido = archivo.readlines()

X = contenido[3:3+int(contenido[1])]
X = [i.split("\t") for i in X]
X = [list(map(int, i)) for i in X]


Y = contenido[3+int(contenido[1]):]
Y = [i.split("\t") for i in Y]
Y = [list(map(int, i)) for i in Y]

X = n.array(X)
Y = n.array(Y)


Clases = ["BASQUETBOL", "FUTBOL", "VOLEIBOL"]


n_splits = 7  # folds
indices = n.arange(X.shape[1])  # Índices de los casos
n.random.shuffle(indices)
fold_size = len(indices) // n_splits

fold = 1
total_casos_correctos = 0
total_casos_analizados = 0

print("Metodo Cross Validation \n")

for i in range(n_splits):
    print(f"Fold {fold}:")
    fold += 1

    # Dividir los índices en entrenamiento y prueba
    test_indices = indices[i * fold_size:(i + 1) * fold_size]
    train_indices = n.setdiff1d(indices, test_indices)

    # Dividir los datos en entrenamiento y prueba
    X_train, X_test = X[:, train_indices], X[:, test_indices]
    Y_train, Y_test = Y[:, train_indices], Y[:, test_indices]

    # Entrenamiento
    Paso1 = X_train.dot(X_train.T)
    Paso2 = n.linalg.inv(Paso1)
    Xpseudo = X_train.T.dot(Paso2)
    W = Y_train.dot(Xpseudo)

    # Evaluación
    casos_correctos = 0
    for j in range(X_test.shape[1]):  # Para cada caso de prueba
        casoi = X_test[:, j]
        Ycasoi = W.dot(casoi)
        Yrealcasoi = Y_test[:, j]

        IndexMaxYcasoi = list(Ycasoi).index(max(Ycasoi))
        IndexMaxYrealcasoi = list(Yrealcasoi).index(max(Yrealcasoi))

        if IndexMaxYcasoi == IndexMaxYrealcasoi:
            casos_correctos += 1

        print(f"  Caso {j + 1}:")
        print(f"    Clase Asignada: {Clases[IndexMaxYcasoi]}")
        print(f"    Clase Real: {Clases[IndexMaxYrealcasoi]}")

    # Resultados del fold
    total_casos_correctos += casos_correctos
    total_casos_analizados += X_test.shape[1]
    print(f"  Casos Correctos en Fold: {casos_correctos}/{X_test.shape[1]}\n")

# Resultados finales
eficiencia = (total_casos_correctos / total_casos_analizados) * 100.0
print("Resultados Finales:")
print(f"  Total de Casos Analizados: {total_casos_analizados}")
print(f"  Total de Casos Correctos: {total_casos_correctos}")
print(f"  Eficiencia del Asociador Lineal: {eficiencia:.2f}%")