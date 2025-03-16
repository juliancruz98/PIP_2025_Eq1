import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P18_Checkbox_v2.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.cb_Dormir.clicked.connect(self.control) #Pasatiempos
        self.cb_Jugar.clicked.connect(self.control)
        self.cb_Salir.clicked.connect(self.control)

        self.cb_Cine.clicked.connect(self.control)  #Lugares Favoritos
        self.cb_Playa.clicked.connect(self.control)
        self.cb_Plazas.clicked.connect(self.control)

    #Area de los slots
    def control(self):
        obj=self.sender()
        valor = obj.isChecked()
        print("Objeto",obj.text(),": ",valor)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())