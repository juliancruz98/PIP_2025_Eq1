import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E05_Ahorcado.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #Area de los signals
        self.btn_comprobar.clicked.connect(self.comprobar)
        self.btn_empezar.clicked.connect(self.empezar)

        #contador de las vidas restantes
        self.oportunidades = 5


    #Area de los slots
    def empezar(self):
        self.palabra = self.box.text()
        self.oculta_palabra = '*' * len(self.palabra)
        self.box.setText(self.oculta_palabra)

        self.respuesta_box.clear()

        self.oportunidades = 5

        self.label_vidas.setText(f"Vidas restantes: {self.oportunidades}")

        self.btn_comprobar.setText("Comprobar")
        self.btn_comprobar.clicked.disconnect()
        self.btn_comprobar.clicked.connect(self.comprobar)

    def comprobar(self):
        try:
            respuesta = self.respuesta_box.text()

            if respuesta == self.palabra:
                self.msj("¡Correcto!")
            else:
                self.msj("Incorrecto.")

            self.oportunidades -= 1

            self.label_vidas.setText(f"Vidas restantes: {self.oportunidades}")

            if self.oportunidades <= 0:
                self.msj(f"La palabra era: {self.palabra}")
                QtCore.QCoreApplication.quit()

        except ValueError:
            self.msj("Por favor, ingrese una respuesta válida.")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
