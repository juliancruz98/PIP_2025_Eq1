import sys
import time as t
from PyQt5 import uic, QtWidgets,QtCore,QtGui
qtCreatorFile = "P12_RadiusButton_GroupBox.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.rb_perro.clicked.connect(self.perro)
        self.rb_gato.clicked.connect(self.gato)
        self.rb_hamster.clicked.connect(self.hamster)


        #groupbox 2
        self.rb_negro.toggled.connect(self.negro)
        self.rb_rojo.toggled.connect(self.rojo)
        self.rb_azul.toggled.connect(self.azul)


    #Area de los slots
    def perro(self):
        print("perro")

    def gato(self):
        print("gato")

    def hamster(self):
        print("hamster")


    def rojo(self):
        v = self.rb_rojo.isChecked()
        print("rojo", v)

    def azul(self):
        v = self.rb_azul.isChecked()
        print("azul", v)

    def negro(self):
        v = self.rb_negro.isChecked()
        print("negro", v)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())