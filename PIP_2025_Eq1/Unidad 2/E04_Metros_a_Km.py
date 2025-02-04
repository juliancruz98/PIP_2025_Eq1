import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E04_Metros_a_Km.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.dial.valueChanged.connect(self.cambiaValor)
        self.dial.setMinimum(-2000)
        self.dial.setMaximum(2000)
        self.dial.setSingleStep(5)
        self.dial.setValue(0)
        self.dial.setWrapping(True)

    #Area de los slots
    def cambiaValor(self):
        metros = self.dial.value()
        kilometros = metros / 1000
        self.txt_metros.setText(str(metros))
        self.txt_kms.setText(str(round(kilometros, 3)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())