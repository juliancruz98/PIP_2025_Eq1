import sys
import random
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E06_Gato.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Inicializar turno aleatorio
        self.turno = random.choice(["X", "O"])
        self.lbl_turno.setText(f"Turno de {self.turno}")

        self.botones = [
            [self.btn01, self.btn02, self.btn03],
            [self.btn04, self.btn05, self.btn06],
            [self.btn07, self.btn08, self.btn09]
        ]

        for fila in self.botones:
            for boton in fila:
                boton.clicked.connect(self.jugar)

        self.btn_Reiniciar.clicked.connect(self.reiniciar)

        # Si la computadora juega primero
        self.jugada_computadora()

    def jugar(self):
        boton = self.sender()
        if boton.text() == "":
            boton.setText(self.turno)
            if self.verificar_ganador():
                return
            self.turno = "X" if self.turno == "O" else "O"
            self.lbl_turno.setText(f"Turno de {self.turno}")
            self.jugada_computadora()

    def verificar_ganador(self):
        for fila in self.botones:
            if fila[0].text() == fila[1].text() == fila[2].text() != "":
                self.ganador(fila[0].text())
                return True

        for i in range(3):
            if self.botones[0][i].text() == self.botones[1][i].text() == self.botones[2][i].text() != "":
                self.ganador(self.botones[0][i].text())
                return True

        if self.botones[0][0].text() == self.botones[1][1].text() == self.botones[2][2].text() != "":
            self.ganador(self.botones[0][0].text())
            return True

        if self.botones[0][2].text() == self.botones[1][1].text() == self.botones[2][0].text() != "":
            self.ganador(self.botones[0][2].text())
            return True

        return False

    def ganador(self, jugador):
        QtWidgets.QMessageBox.information(self, "Ganador", f"El jugador {jugador} ha ganado")
        self.reiniciar()

    def reiniciar(self):
        self.turno = random.choice(["X", "O"])
        self.lbl_turno.setText(f"Turno de {self.turno}")
        for fila in self.botones:
            for boton in fila:
                boton.setText("")
        self.jugada_computadora()

    def jugada_computadora(self):
        if self.turno == "O":
            casillas_libres = [boton for fila in self.botones for boton in fila if boton.text() == ""]
            if casillas_libres:
                boton = random.choice(casillas_libres)
                boton.setText("O")
                if self.verificar_ganador():
                    return
                self.turno = "X"
                self.lbl_turno.setText("Turno de X")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())