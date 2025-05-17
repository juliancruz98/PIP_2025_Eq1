#este si va ejecuta p1 ejemplo

import sys
from PyQt5 import uic, QtWidgets
# qtCreatorFile = "P04_SumaDosNumeros.ui" #Nombre del archivo aquí.
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

import P1_verPython_Ejemplo as interfaz

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.btn_suma.clicked.connect(self.sumar)

    #Area de los slots
    def sumar(self):
        try:
            a = int(self.txt_numero1.text())
            b = int(self.txt_numero2.text())
            r=a+b
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