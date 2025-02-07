import sys
import time as t
from PyQt5 import uic, QtWidgets,QtCore,QtGui
qtCreatorFile = "P10_SegundoPlano.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.btn_temporizar.clicked.connect(self.temporizar2doPlano)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.controlSegundoPlano)
        self.valorN = -1

    #Area de los slots
    def controlSegundoPlano(self):
        self.txt_temporizador.setText(str(self.valorN))
        self.valorN -= 1
        if self.valorN == -1:
            self.segundoPlano.stop()

    def temporizar2doPlano(self):
        self.valorN = int(self.txt_temporizador.text())
        self.segundoPlano.start(500)


    def temporizar(self):
        valor = int(self.txt_temporizador.text())
        for i in range(valor, 0, -1):
            self.txt_temporizador.setText(str(i))
            print(i)
            t.sleep(0.5)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())