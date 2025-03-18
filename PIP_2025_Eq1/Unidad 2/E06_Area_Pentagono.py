import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E06_Area_Pentagono.ui" #Nombre del archivo aquí.
#p05 componentes picsmap
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.dial.valueChanged.connect(self.calcularArea)
        self.dial.setMinimum(0)
        self.dial.setMaximum(200)
        self.dial.setSingleStep(1)
        self.dial.setValue(0)
        self.dial.setWrapping(True)

        self.dial_2.valueChanged.connect(self.calcularArea)
        self.dial_2.setMinimum(0)
        self.dial_2.setMaximum(200)
        self.dial_2.setSingleStep(1)
        self.dial_2.setValue(0)
        self.dial_2.setWrapping(True)

    #Area de los slots
    def calcularArea(self):
        perimetro = self.dial.value()
        apotema = self.dial_2.value()
        area = (perimetro * apotema) / 2
        self.txt_perimetro.setText(str(perimetro))
        self.txt_apotema.setText(str(apotema))
        self.txt_area.setText(str(area))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())