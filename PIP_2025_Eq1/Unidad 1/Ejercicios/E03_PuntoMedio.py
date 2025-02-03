import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E03_PuntoMedio.ui" # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los signals
        self.btn_Calcular.clicked.connect(self.calcular)

    # Area de los slots
    def calcular(self):
        try:
            x1 = float(self.txt_X1.text())
            y1 = float(self.txt_Y1.text())
            x2 = float(self.txt_X2.text())
            y2 = float(self.txt_Y2.text())
            x = (x1 + x2) / 2
            y = (y1 + y2) / 2
            self.msj("El punto medio es: ("+str(x)+", "+str(y)+")")
        except Exception as error:
            print(error)

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())