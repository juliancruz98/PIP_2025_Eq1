import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E04_ContadorClic.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Area de los signals
        self.btn_temporizar.clicked.connect(self.temporizar2doPlano)
        self.btn_contar.clicked.connect(self.incrementar_contador)

        # Temporizador en segundo plano
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.controlSegundoPlano)
        self.valorN = 0
        self.contador = 0

    # Area de los slots
    # Control del temporizador
    def controlSegundoPlano(self):
        if self.valorN < 0:
            self.segundoPlano.stop()
            self.btn_contar.setEnabled(False) # aqui deshabilitiamos el boton cuando se complete el tiempo
            return

        self.txt_temporizador.setText(str(self.valorN))
        self.valorN -= 1


    def temporizar2doPlano(self):
        self.valorN = int(self.txt_temporizador.text())
        self.contador = 0
        self.lbl_contador.setText("0")
        self.btn_contar.setEnabled(True)
        self.segundoPlano.start(500)

    # Contar clics en el botón
    def incrementar_contador(self):
        self.contador += 1
        self.lbl_contador.setText(str(self.contador))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())