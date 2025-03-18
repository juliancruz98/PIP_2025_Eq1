import sys
from PyQt5 import uic, QtWidgets
import random

qtCreatorFile = "E9_Numero.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Configurar el QSlider
        self.BarraNumero.setRange(0, 100)

        # Conectar el QSlider a su respectivo QLineEdit
        self.BarraNumero.valueChanged.connect(self.actualizar_campo_numero)

        # Conectar el QLineEdit a su respectivo QSlider
        self.CampoNumero.textChanged.connect(self.actualizar_barra_numero)

        # Conectar el botón de adivinar
        self.btn_adivinar.clicked.connect(self.adivinar_numero)

    def actualizar_campo_numero(self):
        self.CampoNumero.setText(str(self.BarraNumero.value()))

    def actualizar_barra_numero(self):
        try:
            valor = int(self.CampoNumero.text())
            self.BarraNumero.setValue(valor)
        except ValueError:
            pass

    def adivinar_numero(self):
        try:
            numero_usuario = int(self.CampoNumero.text())
            if 0 <= numero_usuario <= 100:
                numero_adivinado = random.randint(0, 100)
                if numero_adivinado == numero_usuario:
                    self.resultado.setText(f"¡Adivinaste el número! Era {numero_adivinado}")
                else:
                    self.resultado.setText(f"No adivinaste. El número era {numero_adivinado}")
            else:
                self.msj("Por favor, ingrese un número entre 0 y 100.")
        except ValueError:
            self.msj("Por favor, ingrese un número válido.")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())