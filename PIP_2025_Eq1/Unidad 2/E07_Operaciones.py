import sys
import random
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E07_Operaciones.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Area de los signals
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_sig.clicked.connect(self.siguiente)

        self.tiempo_restante = 0
        self.correctas = 0
        self.incorrectas = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.actualizar_tiempo)

    #Area de los slots
    def iniciar(self):
        try:
            self.tiempo_restante = int(self.camposegundos.text())
            self.restante.setText(f"{self.tiempo_restante} segundos")
            self.generar_ecuacion()
            self.timer.start(1000)  # Actualizar cada segundo
        except ValueError:
            self.msj("Por favor, ingrese un número válido de segundos.")

    def actualizar_tiempo(self):
        self.tiempo_restante -= 1
        self.restante.setText(f"{self.tiempo_restante} segundos")
        if self.tiempo_restante <= 0:
            self.timer.stop()
            self.mostrar_resultados()

    def generar_ecuacion(self):
        operadores = ['+', '-', '*', '/']
        operador = random.choice(operadores)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        if operador == '/':
            num1 = num1 * num2  # Asegurar que la división sea exacta
        self.ecuacion.setText(f"{num1} {operador} {num2}")
        self.resultado_correcto = eval(f"{num1} {operador} {num2}")

    def siguiente(self):
        try:
            respuesta = float(self.campo_respuesta.text())
            if respuesta == self.resultado_correcto:
                self.correctas += 1
            else:
                self.incorrectas += 1
            self.campo_respuesta.clear()
            self.generar_ecuacion()
        except ValueError:
            self.msj("Por favor, ingrese una respuesta válida.")

    def mostrar_resultados(self):
        self.msj(f"Tiempo terminado. Respuestas correctas: {self.correctas}, Respuestas incorrectas: {self.incorrectas}")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())