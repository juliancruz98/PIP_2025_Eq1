import sys
from PyQt5 import uic, QtWidgets
# qtCreatorFile = "P04_SumaDosNumeros.ui" #Nombre del archivo aquí.
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#EJERCICIOS...tomar 10 ejercicios anteriores y convertir el archivo UI a  Archivo py - UNIDAD 4


import P3_vPython_Calcula_IMC as interfaz

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.btn_IMC.clicked.connect(self.sumar)

    #Area de los slots
    def sumar(self):
        try:
            a = int(self.txt_altura.text())
            b = int(self.txt_peso.text())
            c = int(self.txt_numero3.text())
            r=a+b+c
            self.msj("La suma es: "+ str(r))
        except Exception as error:
            print(error)

    def msj(self,txt):
        m=QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())