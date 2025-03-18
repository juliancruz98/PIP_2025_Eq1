import sys
from PyQt5 import uic, QtWidgets
import random

qtCreatorFile = "E09_Num_Aleatorio.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Área de los signals
        self.BarraNumero.setRange(0, 100)
        self.BarraNumero.valueChanged.connect(self.actualizar_campo_numero)
        self.btn_adivinar.clicked.connect(self.adivinar_numero)

    # Área de los slots
    def actualizar_campo_numero(self):
        self.CampoNumero.setText(str(self.BarraNumero.value()))

    def adivinar_numero(self):
        numero_usuario = self.BarraNumero.value()  # Obtiene el valor directamente del slider
        numero_adivinado = random.randint(0, 100)

        if numero_adivinado == numero_usuario:
            self.resultado.setText(f"¡Adivinaste el número! Era {numero_adivinado}")
        else:
            self.resultado.setText(f"No adivinaste. El número era {numero_adivinado}")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())