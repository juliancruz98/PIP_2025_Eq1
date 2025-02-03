import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P07_Componente_horizontalslider.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.horizontalSlider.valueChanged.connect(self.cambiaValor)
        self.horizontalSlider.setMinimum(-100)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setSingleStep(5)
        self.horizontalSlider.setValue(-50)


    #Area de los slots

    def cambiaValor(self):
        value = self.horizontalSlider.value()
        self.txt_Valor.setText(str(value))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())