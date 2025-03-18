import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E05_Peso_a_Dolar.ui" #Nombre del archivo aquí.
#p05 componentes picsmap
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.dial.valueChanged.connect(self.cambiaValor)
        self.dial.setMinimum(1)
        self.dial.setMaximum(200)
        self.dial.setSingleStep(1)
        self.dial.setValue(1)
        self.dial.setWrapping(True)

    #Area de los slots
    def cambiaValor(self):
        pesos = self.dial.value()
        dolares = pesos / 20.5
        self.txt_peso.setText(str(pesos))
        self.txt_dolar.setText(str(round(dolares, 3)))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())