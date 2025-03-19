import sys
import random
from PyQt5 import uic, QtWidgets

qtCreatorFile = "PP03.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Área de los signals
        self.numero_secreto = self.generar_numero_secreto()
        self.intentos = []
        self.btn_enviar.clicked.connect(self.verificar_respuesta)
        self.btn_reiniciar.clicked.connect(self.reiniciar_juego)

    #Area de los signals
    def generar_numero_secreto(self):
        numeros = list(range(10))
        random.shuffle(numeros)
        return numeros[:4]

    def verificar_respuesta(self):
        respuesta = self.txt_respuesta.text()

        if len(respuesta) != 4 or not respuesta.isdigit():
            self.msj("Por favor, ingresa un número de 4 dígitos.")
            return

        if len(set(respuesta)) != 4:
            self.msj("Los números no pueden repetirse.")
            return

        picas, fijas = self.calcular_picas_y_fijas(respuesta)
        self.lbl_resultado.setText(f"Picas: {picas}, Fijas: {fijas}")

        intento = f"{respuesta} - Picas: {picas}, Fijas: {fijas}"
        self.intentos.append(intento)

        # Imprimimos el intento en la consola
        print(self.intentos[-1])

        if isinstance(self.txt_enviados, QtWidgets.QTextEdit):
            self.txt_enviados.setPlainText("\n".join(self.intentos))
        elif isinstance(self.txt_enviados, QtWidgets.QLineEdit):
            self.txt_enviados.setText(" | ".join(self.intentos))

        if fijas == 4:
            self.msj("¡Felicidades has ganado!")

    def calcular_picas_y_fijas(self, respuesta):
        picas = 0
        fijas = 0

        for i in range(4):
            if int(respuesta[i]) == self.numero_secreto[i]:
                fijas += 1

        for i in range(4):
            if int(respuesta[i]) != self.numero_secreto[i] and int(respuesta[i]) in self.numero_secreto:
                picas += 1

        return picas, fijas

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

    def reiniciar_juego(self):
        self.numero_secreto = self.generar_numero_secreto()
        self.intentos.clear()


        self.txt_respuesta.clear()
        self.lbl_resultado.clear()
        if isinstance(self.txt_enviados, QtWidgets.QTextEdit):
            self.txt_enviados.clear()
        elif isinstance(self.txt_enviados, QtWidgets.QLineEdit):
            self.txt_enviados.clear()

        self.msj("Juego reiniciado. Se ha generado un nuevo número secreto.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
