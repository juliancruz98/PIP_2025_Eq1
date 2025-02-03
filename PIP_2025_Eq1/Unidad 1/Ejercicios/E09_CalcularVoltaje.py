import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E09_CalcularVoltaje.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.promedio.clicked.connect(self.calcular_voltaje)

    #Area de los slots
    def calcular_voltaje(self):
        try:
            corriente = float(self.num1.text())
            resistencia = float(self.num2.text())
            voltaje = corriente * resistencia
            self.promedio.setText(f"Voltaje: {round(voltaje, 2)} V")

        except ValueError:
            self.promedio.setText("Por favor, ingrese valores válidos")

    def msj(self,txt):
        m=QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())