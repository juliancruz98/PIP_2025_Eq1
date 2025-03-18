import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E02_Hora_a_Segundos.ui" #Nombre del archivo aquí.

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
        self.dial.setSingleStep(5)
        self.dial.setValue(1)
        self.dial.setWrapping(True)

    #Area de los slots
    def cambiaValor(self):
        horas = self.dial.value()
        segundos = horas * 3600
        self.txt_hrs.setText(str(horas))
        self.txt_sgns.setText(str(segundos))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())