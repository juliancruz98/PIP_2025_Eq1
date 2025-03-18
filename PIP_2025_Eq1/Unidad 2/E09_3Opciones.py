import sys
import random
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E09_Opciones.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.opciones = ["ingeniera", "metal sonic", "bob esponja"]
        self.btn_comprobar.clicked.connect(self.comprobar)
        self.mostrar_opcion_aleatoria()

    #Area de los slots
    def mostrar_opcion_aleatoria(self):
        self.opcion_actual = random.choice(self.opciones)
        self.textorar.setText(self.opcion_actual)

    def comprobar(self):
        indice_correcto = self.opciones.index(self.opcion_actual)
        if self.rb_1.isChecked() and indice_correcto == 0:
            self.msj("¡Correcto!")
        elif self.rb_2.isChecked() and indice_correcto == 1:
            self.msj("¡Correcto!")
        elif self.rb_3.isChecked() and indice_correcto == 2:
            self.msj("¡Correcto!")
        else:
            self.msj("Incorrecto. Inténtalo de nuevo.")


        self.mostrar_opcion_aleatoria()

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
