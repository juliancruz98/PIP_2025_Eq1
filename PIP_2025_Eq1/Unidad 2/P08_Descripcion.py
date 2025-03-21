import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P08_Descripcion.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.SelectorImagen.valueChanged.connect(self.cambiaValor)
        self.SelectorImagen.setMinimum(0)
        self.SelectorImagen.setMaximum(2)
        self.SelectorImagen.setSingleStep(1)
        self.SelectorImagen.setValue(0)

        self.diccionarDatos = {
            0: (":/ejercicios/elyochi.jpg",["MetalSonic","juego","1"]),
            1: (":/ejercicios/kaldo.jpg", ["grinchazul", "pelicula", "2"]),
            2: (":/ejercicios/wero.jpg", ["bobesponja", "caricatura", "3"])
        }

        self.indice = 0
        self.obtenerDatos()

    #Area de los slots
    def obtenerDatos(self):
        nombre = self.diccionarDatos[self.indice][1][0]
        contexto = self.diccionarDatos[self.indice][1][1]
        numero = self.diccionarDatos[self.indice][1][2]
        self.txt_NombreIma.setText(nombre)
        self.txt_ContexIma.setText(contexto)
        self.txt_N.setText(numero)
        print(nombre, contexto, numero)

    def cambiaValor(self):
        self.indice = self.SelectorImagen.value()
        self.obtenerDatos()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())