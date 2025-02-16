import sys
import time as t
from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "PP01.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Lista de imágenes para cambiar
        self.imagenes = [":/ejercicios/cat.jpeg", ":/ejercicios/duolingo.jpeg", ":/ejercicios/elyochi.jpg", ":/ejercicios/hermanosgold.jpeg", ":/ejercicios/kaldo.jpg"]  # Cambia con tus imágenes
        self.indice_imagen = 0  # Índice actual de la imagen

        # Configurar QLabel con la primera imagen
        self.lbl_imagen.setPixmap(QtGui.QPixmap(self.imagenes[self.indice_imagen]))

        # Configurar el temporizador
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.cambiarImagen)
        self.segundoPlano.start(500)  # Cambia la imagen cada 2 segundos

    def cambiarImagen(self):
        self.indice_imagen = (self.indice_imagen + 1) % len(self.imagenes)  # Ciclo de imágenes
        self.lbl_imagen.setPixmap(QtGui.QPixmap(self.imagenes[self.indice_imagen]))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
