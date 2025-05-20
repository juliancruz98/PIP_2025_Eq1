import sys
import serial as tarjeta
from PyQt5 import uic, QtWidgets

qtCreatorFile3 = "DialogoConexionArduino.ui"
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self, referencia_a_main):
        super().__init__()
        self.setupUi(self)

        self.principal = referencia_a_main
        self.btn_accion.clicked.connect(self.accion)

    def accion(self):
        try:
            texto = self.btn_accion.text()
            com = self.txt_com.text()

            if texto == "CONECTAR":
                self.principal.arduino = tarjeta.Serial(com, baudrate=9600, timeout=1)
                self.principal.segundoPlano.start(100)
                self.btn_accion.setText("DESCONECTAR")
                self.principal.txt_estado.setText("CONECTADO")

            elif texto == "DESCONECTAR":
                self.principal.segundoPlano.stop()
                self.principal.arduino.close()
                self.btn_accion.setText("RECONECTAR")
                self.principal.txt_estado.setText("DESCONECTADO")

            elif texto == "RECONECTAR":
                try:
                    self.principal.arduino.open()
                    self.principal.segundoPlano.start(100)
                    self.btn_accion.setText("DESCONECTAR")
                    self.principal.txt_estado.setText("RECONECTADO")
                except Exception as e:
                    QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo reconectar:\n{e}")

        except Exception as error:
            QtWidgets.QMessageBox.critical(self, "Error de conexión", f"{error}")
            self.principal.txt_estado.setText("ERROR")
