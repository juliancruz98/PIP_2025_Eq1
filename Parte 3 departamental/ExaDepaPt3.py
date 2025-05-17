import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt, QTimer
import serial

qtCreatorFile = "DiseñoParte3.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.estado_led = self.findChild(QtWidgets.QLabel, 'estado_led')
        self.progressBar = self.findChild(QtWidgets.QProgressBar, 'progressBar')
        self.umbral = 600

        self.serial_port = serial.Serial('COM7', 9600)
        self.timer = QTimer()
        self.timer.timeout.connect(self.leer_datos_arduino)
        self.timer.start(500)

    def actualizar_estado_led(self, estado):
        if self.estado_led:
            self.estado_led.setText(estado.upper())

    def actualizar_progressBar(self, valor):
        if self.progressBar:
            self.progressBar.setValue(valor)
            self.progressBar.setMaximum(1023)

    def leer_datos_arduino(self):
        if self.serial_port and self.serial_port.in_waiting > 0:
            while self.serial_port.in_waiting > 0:
                line = self.serial_port.readline().decode('utf-8').rstrip()
                if line.startswith("Valor fotoresistencia: "):
                    valor_luz = int(line.split(": ")[1])
                    self.actualizar_progressBar(valor_luz)
                    if valor_luz < self.umbral:
                        self.actualizar_estado_led("encendido")
                    else:
                        self.actualizar_estado_led("apagado")
                elif line.startswith("LED: "):
                    estado_led = line.split(": ")[1]
                    self.actualizar_estado_led(estado_led)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())