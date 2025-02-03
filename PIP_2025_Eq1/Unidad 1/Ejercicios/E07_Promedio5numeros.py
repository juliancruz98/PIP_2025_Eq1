import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E07_Promedio5Numeros.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.promedio.clicked.connect(self.calcularprom)

    #Area de los slots
    def calcularprom(self):
        try:
            numeros = [
                float(self.num1.text()),
                float(self.num2.text()),
                float(self.num3.text()),
                float(self.num4.text()),
                float(self.num5.text())
            ]
            suma = sum(numeros)
            promedio = suma / len(numeros)
            self.promedio.setText(f"Promedio: {round(promedio,2)}")
        except ValueError:
            self.promedio.setText("Por favor, ingrese números válidos.")

    def msj(self,txt):
        m=QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())