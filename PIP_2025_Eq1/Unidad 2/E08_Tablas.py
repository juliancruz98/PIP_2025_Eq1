import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E08_Tablas.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los signals
        self.dial.valueChanged.connect(self.actualizarTabla)
        self.dial.setMinimum(1)
        self.dial.setMaximum(10)
        self.dial.setSingleStep(1)
        self.dial.setValue(1)

    #Area de los slots
    def actualizarTabla(self):
        numero = self.dial.value()
        self.txt_num.setText(str(numero))

        self.label_01.setText(f"{numero} x 1 ="), self.label_06.setText(f"{numero} x 6 =")
        self.label_02.setText(f"{numero} x 2 ="), self.label_07.setText(f"{numero} x 7 =")
        self.label_03.setText(f"{numero} x 3 ="), self.label_08.setText(f"{numero} x 8 =")
        self.label_04.setText(f"{numero} x 4 ="), self.label_09.setText(f"{numero} x 9 =")
        self.label_05.setText(f"{numero} x 5 ="), self.label_010.setText(f"{numero} x 10 =")


        resultados = [
            self.txt_num1, self.txt_num2, self.txt_num3, self.txt_num4,
            self.txt_num5, self.txt_num6, self.txt_num7, self.txt_num8,
            self.txt_num9, self.txt_num10
        ]

        for i in range(10):
            resultados[i].setText(str(numero * (i + 1)))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
