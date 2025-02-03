import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P03_EjemploLineEdit.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.btn_saludar.clicked.connect(self.saludar)

    #Area de los slots
    def saludar (self):
        cadena = self.txt_nombre.text()
        if cadena !="":
            self.msj("Hola "+cadena+", buen dia xD")
        else:
            self.msj("Primero debes ingresar un nombre")

    def msj(self,txt):
        m=QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())