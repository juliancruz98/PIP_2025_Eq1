import sys
import random as rnd
from matplotlib import pyplot as plt
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "P00_intro.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.btn_graficar.clicked.connect(self.graficar)
        self.segundoPlano = QtCore.QTimer()
        self.btn_graficar.clicked.connect(self.graficar)

        self.x = [i for i in range(11)] #se cambia el 11 por otro valor para que se vea como un electrocardiograma
        self.y = []


    #Area de los slots
    def lecturas (self):
        #tarea hacer esto mismo pero con un sensor
        #que nosotros querramos ultrasonic
        while len(self.y) < self.x:
            t = rnd.randint(0, 1023) #esta se cambiaria
            self.y.append(t)
        #solamente se cambian estas lineas de arriba

        print(self.x)
        print(self.y)

        self.ax.plot(self.x, self.y)
        self.canvas.draw()

        plt.cla()
        del self.y[0]


    def graficar(self):
        pass




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())