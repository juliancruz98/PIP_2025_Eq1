import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E08_Velocidad.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.promedio.clicked.connect(self.calcular_velocidad)

    #Area de los slots
    def calcular_velocidad(self):
        try:
            distancia = float(self.distancia.text())
            tiempo = float(self.tiempo.text())
            if tiempo == 0:
                self.promedio.setText("El tiempo no puede ser cero")
            else:
                velocidad = distancia / tiempo
                self.promedio.setText(f"Velocidad: {round(velocidad, 2)} m/s")
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