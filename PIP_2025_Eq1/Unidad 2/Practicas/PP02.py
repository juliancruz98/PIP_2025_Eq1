import time as t
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "P02_selectorCompuertasLogicasl.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.txt_a.textChanged.connect(self.determinar_compuerta)
        self.txt_b.textChanged.connect(self.determinar_compuerta)

    # Área de los Slot
    def determinar_compuerta(self):
        a = self.txt_a.text()
        b = self.txt_b.text()

        # Validar que los inputs son 0 o 1
        if a not in ['0', '1'] or b not in ['0', '1']:
            self.txt_compuerta.setText("")
            return

        # Convertir a booleanos (True/False)
        a_bool = a == '1'
        b_bool = b == '1'

        # Calcular salida para cada compuerta
        and_out = a_bool and b_bool
        or_out = a_bool or b_bool
        xor_out = a_bool != b_bool
        nand_out = not (a_bool and b_bool)
        nor_out = not (a_bool or b_bool)
        xnor_out = not (a_bool != b_bool)

        # Determinar qué compuertas dan salida 1
        compuertas = []
        if and_out:
            compuertas.append("AND")
        if or_out:
            compuertas.append("OR")
        if xor_out:
            compuertas.append("XOR")
        if nand_out:
            compuertas.append("NAND")
        if nor_out:
            compuertas.append("NOR")
        if xnor_out:
            compuertas.append("XNOR")

        # Mostrar las compuertas resultantes
        if compuertas:
            self.txt_compuerta.setText(", ".join(compuertas))
        else:
            self.txt_compuerta.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())