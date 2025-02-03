import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P05_SumaDosNumerosV2.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.btn_sumar.clicked.connect(self.sumar)

    #Area de los slots
    def sumar(self):
        try:
            a = float(self.txt_A.text())
            b = float(self.txt_B.text())
            r=a+b
            #self.msj("La suma es: "+ str(r))
            self.txt_resultado.setText(str(r))
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