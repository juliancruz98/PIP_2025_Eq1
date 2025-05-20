from PyQt5 import uic, QtWidgets

qtCreatorFile3 = "DialogoConexionArduinoV2.ui"
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)


class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self, referencia_a_main):
        super().__init__()
        self.setupUi(self)
        self.principal = referencia_a_main
        self.btn_accion.clicked.connect(self.accion)

        # Verificar si ya está conectado al abrir el diálogo
        if self.principal.arduino and self.principal.arduino.is_open:
            self.btn_accion.setText("DESCONECTAR")
            self.txt_com.setText(self.principal.arduino.port)
            self.txt_com.setEnabled(False)
        else:
            self.btn_accion.setText("CONECTAR")
            self.txt_com.setEnabled(True)

    def accion(self):
        try:
            texto = self.btn_accion.text()
            com = self.txt_com.text()

            if texto == "CONECTAR":
                self.principal.conectar_puerto(com)
                self.btn_accion.setText("DESCONECTAR")
                self.txt_com.setEnabled(False)
                self.principal.txt_estado.setText("CONECTADO")

            elif texto == "DESCONECTAR":
                self.principal.detener_lector_serial()
                if self.principal.arduino:
                    self.principal.arduino.close()
                self.btn_accion.setText("RECONECTAR")
                self.txt_com.setEnabled(True)
                self.principal.txt_estado.setText("DESCONECTADO")

            elif texto == "RECONECTAR":
                try:
                    if self.principal.arduino:
                        self.principal.arduino.open()
                        self.principal.iniciar_lector_serial()
                        self.btn_accion.setText("DESCONECTAR")
                        self.txt_com.setEnabled(False)
                        self.principal.txt_estado.setText("RECONECTADO")
                except Exception as e:
                    QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo reconectar:\n{e}")

        except Exception as error:
            QtWidgets.QMessageBox.critical(self, "Error de conexión", f"{error}")
            self.principal.txt_estado.setText("ERROR")
