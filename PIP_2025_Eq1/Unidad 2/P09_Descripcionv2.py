import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P09_Descripcionv2.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.SelectorImagen.setMinimum(1)
        self.SelectorImagen.setMaximum(3)
        self.SelectorImagen.setSingleStep(1)
        self.SelectorImagen.setValue(1)
        self.SelectorImagen.valueChanged.connect(self.cambiaValor)

        self.diccionarioDatos = {
            1: (":/ejercicios/elyochi.jpg",["Metal Sonic","Meme","Erizo"]),
            2: (":/ejercicios/kaldo.jpg", ["Grinch azul", "Meme", "chango"]),
            3: (":/ejercicios/wero.jpg", ["Bob Esponja", "Meme", "esponja"])
        }
        self.indice = 1
        self.obtenerDatos()

    #Area de los slots
    def obtenerDatos(self):
        nombre = self.diccionarioDatos[self.indice][1][0]
        contexto = self.diccionarioDatos[self.indice][1][1]
        numero = self.diccionarioDatos[self.indice][1][2]
        self.txt_nombreimagen.setText(nombre)
        self.txt_contextoimagen.setText(contexto)
        self.txt_numero.setText(numero)
        self.imagen_Desc.setPixmap(QtGui.QPixmap(self.diccionarioDatos[self.indice][0]))

    def cambiaValor(self):
        self.indice = self.SelectorImagen.value()
        self.obtenerDatos()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())