import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E02_Metros_a_Pies.ui" # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los signals
        self.btn_Transformar.clicked.connect(self.calcular)

    # Area de los slots
    def calcular(self):
        try:
            metros = float(self.txt_Metros.text())
            pies = metros * 3.28084
            self.msj("Tu medida en pies es: "+str(pies))

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