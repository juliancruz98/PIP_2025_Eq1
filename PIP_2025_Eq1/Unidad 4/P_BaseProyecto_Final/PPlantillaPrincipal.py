import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
import serial as tarjeta
import DialogoConexionArduino

qtCreatorFile = "BaseProyectoServicios.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.txt_com.setText("COM7")  # Ajusta según tu sistema
        self.arduino = None

        self.btn_inicial.clicked.connect(self.inicializar)
        self.btn_led1.clicked.connect(self.control)
        self.btn_led2.clicked.connect(self.control)
        self.btn_led3.clicked.connect(self.control)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)

        self.bandera = 0
        self.datos = []

    def inicializar(self):
        self.dialogo = DialogoConexionArduino.MyDialog(self)
        self.dialogo.show()

    def control(self):
        obj = self.sender()
        texto = obj.text()
        led = obj.objectName()[-1]
        try:
            if self.arduino and self.arduino.isOpen():
                if texto == "PRENDER":
                    obj.setText("APAGAR")
                    c = led + "1"
                    self.arduino.write(c.encode())
                else:
                    obj.setText("PRENDER")
                    c = led + "0"
                    self.arduino.write(c.encode())
        except Exception as e:
            print(f"Error al enviar datos al Arduino: {e}")
            self.txt_estado.setText("ERROR")
            self.segundoPlano.stop()

    def lecturas(self):
        try:
            if self.arduino and self.arduino.isOpen():
                if self.arduino.inWaiting():
                    cadena = self.arduino.readline().decode().strip()
                    if cadena:
                        self.datos.append(cadena)
                        if self.bandera == 0:
                            self.lista_datos.addItem(cadena)
                            cadena = cadena.split(" - ")[:-1]
                            cadena = [int(i) for i in cadena]
                            self.lista_datos.addItem(str(cadena))
                            self.lista_datos.setCurrentRow(self.lista_datos.count() - 1)
            else:
                print("Arduino no conectado")
        except Exception as e:
            print(f"Error durante la lectura: {e}")
            self.txt_estado.setText("ERROR")
            self.segundoPlano.stop()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
