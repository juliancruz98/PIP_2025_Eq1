import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E05_AreaRectangulo.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.btn_calcular.clicked.connect(self.calcular)

    #Area de los slots
    def calcular(self):
        try:
            base = float(self.txt_base.text())
            altura= float(self.txt_altura.text())
            resultado=base*altura
            self.msj("El  area del Rectangulo es: "+ str(resultado))

            # para reiniciar los campos
            self.txt_altura.setText("")
            self.txt_base.setText("")

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