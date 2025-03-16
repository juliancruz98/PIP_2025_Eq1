import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P17_Checkbox.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.cb_Dormir.clicked.connect(self.Dormir)
        self.cb_Cine.clicked.connect(self.Cine)

    #Area de los slots
    def Dormir(self):
        valor = self.cb_Dormir.isChecked()
        print("Dormir",valor)

    def Cine(self):
        valor = self.cb_Cine.isChecked()
        print("Cine",valor)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())