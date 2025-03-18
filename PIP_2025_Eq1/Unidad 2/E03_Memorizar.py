import sys
import random
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E03_Memorizar.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Area de los signals
        self.btn_inicio.clicked.connect(self.empezar)
        self.btn_reiniciar.clicked.connect(self.reiniciar)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.mostrar_ocultar_imagenes)


        self.lapso_timer = QtCore.QTimer()
        self.lapso_timer.timeout.connect(self.terminar_lapso)


        self.contador_imagen1 = 0
        self.contador_imagen2 = 0

    #Area de los slots
    def empezar(self):
        self.contador_imagen1 = 0
        self.contador_imagen2 = 0

        self.timer.start(500)

        self.lapso_timer.start(5000)

        self.btn_inicio.setText("Comprobar")
        self.btn_inicio.clicked.disconnect()
        self.btn_inicio.clicked.connect(self.comprobar)

    def reiniciar(self):
        self.timer.stop()
        self.lapso_timer.stop()

        self.image_1.setVisible(False)
        self.image_2.setVisible(False)

        self.no_imagen1.clear()
        self.no_imagen2.clear()

        self.btn_inicio.setText("Empezar")
        self.btn_inicio.clicked.disconnect()
        self.btn_inicio.clicked.connect(self.empezar)

    def mostrar_ocultar_imagenes(self):
        if random.choice([True, False]):
            self.image_1.setVisible(True)
            self.contador_imagen1 += 1
        else:
            self.image_1.setVisible(False)

        if random.choice([True, False]):
            self.image_2.setVisible(True)
            self.contador_imagen2 += 1
        else:
            self.image_2.setVisible(False)

    def terminar_lapso(self):
        self.timer.stop()

        self.image_1.setVisible(True)
        self.image_2.setVisible(True)


        self.no_imagen1.setEnabled(True)
        self.no_imagen2.setEnabled(True)

        self.btn_inicio.setText("Comprobar")
        self.btn_inicio.clicked.disconnect()
        self.btn_inicio.clicked.connect(self.comprobar)

    def comprobar(self):
        try:
            respuesta_imagen1 = int(self.no_imagen1.text())
            respuesta_imagen2 = int(self.no_imagen2.text())

            if respuesta_imagen1 == self.contador_imagen1 and respuesta_imagen2 == self.contador_imagen2:
                self.msj("¡Correcto!")
            else:
                self.msj(f"Incorrecto. Imagen 1: {self.contador_imagen1} veces, Imagen 2: {self.contador_imagen2} veces")

        except ValueError:
            self.msj("Por favor, ingrese números válidos.")



    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())