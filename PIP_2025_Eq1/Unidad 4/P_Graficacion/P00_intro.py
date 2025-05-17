import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P00_intro.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.btn_graficar.clicked.connect(self.graficar)


    #Area de los slots


    def graficar(self):
        x = [i for i in range(11)]

        import random as rnd

        y =[]
        for i in x:
            t = rnd.randint(0,1023)
            y.append(t)
        print(x)
        print(y)

        self.ax.plot(x, y)
        self.canvas.draw()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())