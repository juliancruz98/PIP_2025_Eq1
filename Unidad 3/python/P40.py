import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
import serial as tarjeta

qtCreatorFile = "P40.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Área de inicialización
        self.arduino = None
        self.datos = []  # Lista para almacenar datos recibidos
        self.bandera = 0  # Variable de control

        # Área de los signals
        self.txt_com.setText("COM7")
        self.btn_accion.clicked.connect(self.accion)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)
        self.btn_control.clicked.connect(self.control)

    # Área de los slots
    def control(self):
        texto = self.btn_control.text()
        if self.arduino.isOpen:
            if texto == "PRENDER":
                self.btn_control.setText("APAGAR")
                self.arduino.write("1".encode())
            else:
                self.btn_control.setText("PRENDER")
                self.arduino.write("0".encode())


    def lecturas(self):
        if self.arduino.isOpen():
            if self.arduino.inWaiting():
                cadena = self.arduino.readline().decode().strip()
                if cadena != "":
                    self.datos.append(cadena)
                    if self.bandera ==0:
                        print(cadena)
                        self.lista_datos.addItem(cadena)
                        self.lista_datos.setCurrentRow(self.lista_datos.count()-1)

    


    def accion(self):
        texto = self.btn_accion.text()
        com = self.txt_com.text()

        try:
            if texto == "CONECTAR":
                self.arduino = tarjeta.Serial(com, baudrate=9600, timeout=1)
                self.segundoPlano.start(100)
                self.btn_accion.setText("DESCONECTAR")
                self.txt_estado.setText("CONECTADO")
            elif texto == "DESCONECTAR":
                if self.arduino and self.arduino.isOpen():
                    self.segundoPlano.stop()
                    self.arduino.close()
                self.btn_accion.setText("RECONECTAR")
                self.txt_estado.setText("DESCONECTADO")
            elif texto == "RECONECTAR":
                if self.arduino:
                    self.arduino.open()
                    self.segundoPlano.start(100)
                    self.btn_accion.setText("DESCONECTAR")
                    self.txt_estado.setText("RECONECTADO")
        except Exception as e:
            print(f"Error en la conexión: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())