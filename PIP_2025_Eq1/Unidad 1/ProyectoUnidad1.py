import sys, os
from PyQt5 import uic, QtWidgets
qtCreatorFile = "ProyectoUnidad1.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        #botoenes de interacción
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.btn_cargar.clicked.connect(self.cargar)


        self.valores = []

    #Area de los slots
    def cargar(self):
        try:
            with open("prueba1.csv", "r") as archivo:
                lineas = archivo.readlines()
                self.valores = []
                for linea in lineas:
                    if linea.startswith("Valores:"):
                        continue
                    elif linea.startswith("Promedio:"):
                        self.prom = float(linea.split(":")[1].strip())
                    elif linea.startswith("Menor Valor:"):
                        self.menor = int(linea.split(":")[1].strip())
                    elif linea.startswith("Mayor Valor:"):
                        self.mayor = int(linea.split(":")[1].strip())
                    elif linea.startswith("Mediana:"):
                        self.med = float(linea.split(":")[1].strip())
                    elif linea.startswith("Moda:"):
                        modas = linea.split(":")[1].strip().strip("[]").split(", ")
                        self.modas = [int(m) for m in modas]
                    elif linea.startswith("Varianza:"):
                        self.varianza = float(linea.split(":")[1].strip())
                    elif linea.startswith("Desviación Estándar:"):
                        self.desviacion = float(linea.split(":")[1].strip())
                    else:
                        self.valores.append(int(linea.strip()))
                self.actualizarcajas()
                self.msj("Archivo cargado con éxito!!!")
        except Exception as e:
            self.msj(f"Error al cargar el archivo: {e}")

    def agregar(self):
        try:
            valores = int(self.txt_valores.text())
            self.valores.append(valores)
            self.promedio()
            self.txt_linea_valores.setText(str(self.valores))
            self.actualizarcajas()
        except ValueError:
            self.msj("Por favor, ingresa solo números.")

    def guardar(self):
        try:
            with open("prueba1.csv", "w") as archivo:
                archivo.write("Valores:\n")
                for c in self.valores:
                    archivo.write(str(c) + '\n')
                archivo.write(f"Promedio: {self.prom}\n")
                archivo.write(f"Menor Valor: {self.menorvalor()}\n")
                archivo.write(f"Mayor Valor: {self.mayorvalor()}\n")
                archivo.write(f"Mediana: {self.mediana()}\n")
                archivo.write(f"Moda: {self.moda()}\n")
                archivo.write(f"Varianza: {self.calcular_varianza()}\n")
                archivo.write(f"Desviación Estándar: {self.desviacion_estandar()}\n")
            self.msj("Archivo guardado con éxito!!!")
        except Exception as e:
            self.msj(f"Error al guardar el archivo: {e}")

    def promedio (self): #ta bien
        prom = round(sum(self.valores) / len(self.valores),2)
        self.txt_promedio.setText(str(prom))
        self.prom=prom

    def menorvalor(self):
           return min(self.valores)

    def mayorvalor(self):
           return max(self.valores)

    def mediana(self):
        if not self.valores:
            return 0

        self.valores.sort()
        n = len(self.valores)
        if n % 2 == 1:  # Si el número de elementos es impar
            return self.valores[n // 2]
        else:  # Si el número de elementos es par
            return (self.valores[n // 2 - 1] + self.valores[n // 2]) / 2

    def moda(self):
        if not self.valores:
            return 0
        frecuencia = {}
        for valor in self.valores:
            if valor in frecuencia:
                frecuencia[valor] += 1
            else:
                frecuencia[valor] = 1
        max_frecuencia = max(frecuencia.values())
        modas = [k for k, v in frecuencia.items() if v == max_frecuencia]
        return modas

    def desviacion_estandar(self):
        if not self.valores or 'prom' not in dir(self):
            return 0
        prom = self.prom
        suma_cuadrados = sum((x - prom) ** 2 for x in self.valores)
        varianza = suma_cuadrados / len(self.valores)
        desviacion = round(varianza ** 0.5, 2)
        return desviacion

    def calcular_varianza(self):
        if not self.valores or 'prom' not in dir(self):
            return 0
        prom = self.prom
        suma_cuadrados = sum((x - prom) ** 2 for x in self.valores)
        varianza = round(suma_cuadrados / len(self.valores),2)
        return varianza

    def actualizarcajas(self):
        self.promedio()
        self.txt_promedio.setText(str(self.prom))

        # Actualizamos el menor y mayor valor
        menor = min(self.valores)
        self.txt_menorvalor.setText(str(menor))

        mayor = max(self.valores)
        self.txt_mayorvalor.setText(str(mayor))

        # Actualizamos la mediana
        mediana = self.mediana()
        self.txt_mediana.setText(str(mediana))

        # Actualizamos la varianza
        varianza = self.calcular_varianza()
        self.txt_varianza.setText(str(varianza))

        # Actualizamos la moda
        modas = self.moda()
        self.txt_moda.setText(str(modas))

        # Actualizamos la desviación estándar
        desviacion = self.desviacion_estandar()
        self.txt_desviacion.setText(str(desviacion))

    def msj(self,txt):
        m=QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())