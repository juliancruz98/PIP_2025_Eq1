import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E07_TeoremaPitagoras.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Area de los signals
        self.BarraCA.valueChanged.connect(self.actualizar_campo_ca)
        self.BarraCB.valueChanged.connect(self.actualizar_campo_cb)
        self.btn_calcular.clicked.connect(self.calcular_hipotenusa)

    # Área de los slots
    def actualizar_campo_ca(self):
        self.CampoCA.setText(str(self.BarraCA.value()))

    def actualizar_campo_cb(self):
        self.CampoCB.setText(str(self.BarraCB.value()))

    def calcular_hipotenusa(self):
        ca = self.BarraCA.value()
        cb = self.BarraCB.value()
        hipo = (ca**2 + cb**2) ** 0.5
        self.hipo.setText(f"{hipo:.2f}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())