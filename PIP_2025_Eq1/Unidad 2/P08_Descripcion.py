import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P08_Descripcion.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.SelectorImagen.valueChanged.connect(self.cambiaValor)
        self.SelectorImagen.setMinimum(1)
        self.SelectorImagen.setMaximum(1)
        self.SelectorImagen.setSingleStep(1)
        self.SelectorImagen.setValue(1)


    #Area de los slots

    def cambiaValor(self):
        value = self.SelectorImagen.value()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())