import sys
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
        archivo = open("../Archivos/prueba1.csv")
        contenido = archivo.readlines()
        datos = [int(x) for x in contenido]
        self.valores = datos
        self.txt_linea_valores.setText(str(self.valores))  # Captura a esto
        self.actualizarcajas()


    def agregar(self):
        valores = int(self.txt_valores.text())
        self.valores.append(valores)
        self.promedio()
        self.txt_linea_valores.setText(str(self.valores))  # Captura a esto
        self.actualizarcajas()



    def guardar(self): #ta bien
        archivo=open("../Archivos/prueba1.csv","w")
        for c in self.valores:
            archivo.write(str(c)+'\n')
        archivo.flush()
        archivo.close()
        self.msj("Archivo guardado con exito!!!")


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
            # Ordenar los valores
        self.valores.sort()
        n = len(self.valores)
        if n % 2 == 1:  # Si el número de elementos es impar
            return self.valores[n // 2]
        else:  # Si el número de elementos es par
            return (self.valores[n // 2 - 1] + self.valores[n // 2]) / 2

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

    def msj(self,txt):
        m=QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())