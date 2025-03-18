import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "E08_Semaforo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los signlas
        # Cargamos las imágenes para las luces
        self.img_rojo = QtGui.QPixmap(":/ejercicios/rojo.jpg")
        self.img_amarillo = QtGui.QPixmap(":/ejercicios/amarillo.jpg")
        self.img_verde = QtGui.QPixmap(":/ejercicios/verde.jpg")

        self.luz_roja = self.findChild(QtWidgets.QLabel, 'lbl_rojo')
        self.luz_amarilla = self.findChild(QtWidgets.QLabel, 'lbl_amarillo')
        self.luz_verde = self.findChild(QtWidgets.QLabel, 'lbl_verde')


        self.luz_verde.setPixmap(self.img_verde)
        self.luz_roja.clear()
        self.luz_amarilla.clear()

        # Configurar el temporizador
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.cambiarLuz)
        self.segundoPlano.start(2000)  # para que cambie  cada 2 segundos xd

        self.estado_semaforo = "Verde"

    #Area de los slots
    def cambiarLuz(self):
        if self.estado_semaforo == "Verde":
            self.luz_verde.clear()
            self.luz_amarilla.setPixmap(self.img_amarillo)
            self.estado_semaforo = "Amarillo"
        elif self.estado_semaforo == "Amarillo":
            self.luz_amarilla.clear()
            self.luz_roja.setPixmap(self.img_rojo)
            self.estado_semaforo = "Rojo"
        else:
            self.luz_roja.clear()
            self.luz_verde.setPixmap(self.img_verde)
            self.estado_semaforo = "Verde"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
