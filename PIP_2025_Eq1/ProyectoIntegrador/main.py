import sys
import serial
import keyboard
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import QThread, pyqtSignal
import DialogoConexionArduino

qtCreatorFile = "ProyectoV2.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class SerialReaderThread(QThread):
    data_received = pyqtSignal(str)

    def __init__(self, arduino):
        super().__init__()
        self.arduino = arduino
        self.running = True

    def run(self):
        while self.running:
            if self.arduino.in_waiting > 0:
                try:
                    line = self.arduino.readline().decode(errors="ignore").strip()
                    self.data_received.emit(line)
                except:
                    pass

    def stop(self):
        self.running = False
        self.wait()

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.arduino = None
        self.serial_thread = None

        self.botones_activos = set()
        self.last_direction = "CENTRO"

        self.txt_estado.setText("SIN CONEXIÓN")
        self.btn_Conectar.clicked.connect(self.abrir_dialogo_conexion)

    def conectar_puerto(self, puerto):
        try:
            self.arduino = serial.Serial(puerto, 9600, timeout=1)
            self.txt_estado.setText(f"CONECTADO ({puerto})")
            self.iniciar_lector_serial()
        except serial.SerialException as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo conectar:\n{e}")
            self.arduino = None

    def iniciar_lector_serial(self):
        if not self.serial_thread or not self.serial_thread.isRunning():
            self.serial_thread = SerialReaderThread(self.arduino)
            self.serial_thread.data_received.connect(self.procesar_entrada)
            self.serial_thread.start()

    def detener_lector_serial(self):
        if self.serial_thread:
            self.serial_thread.stop()
            self.serial_thread = None

    def abrir_dialogo_conexion(self):
        dialogo = DialogoConexionArduino.MyDialog(self)
        dialogo.exec_()

    def procesar_entrada(self, line):
        line = line.strip()

        direcciones = {
            "UP": 'w',
            "DOWN": 's',
            "LEFT": 'a',
            "RIGHT": 'd'
        }

        botones = {
            "Z": "z",
            "X": "x",
            "ENTER": "enter",
            "BACKSPACE": "backspace"
        }

        # --- Movimiento del joystick ---
        if line in direcciones:
            tecla = direcciones[line]
            if self.last_direction != tecla:
                # Soltar solo si hay otra activa
                if self.last_direction in direcciones.values():
                    keyboard.release(self.last_direction)
                keyboard.press(tecla)
                self.last_direction = tecla
                self.txt_joystick.setHtml(f"<center><span style='font-size: 36pt;'>JOYSTICK: {line}</span></center>")

        elif line == "CENTRO":
            if self.last_direction in direcciones.values():
                keyboard.release(self.last_direction)
            self.last_direction = "CENTRO"
            self.txt_joystick.setHtml("<center><span style='font-size: 36pt;'>JOYSTICK: CENTRO</span></center>")
            QtCore.QTimer.singleShot(200, self.txt_joystick.clear)

        # --- Botones A, B, Start, Select ---
        elif line in botones:
            tecla = botones[line]
            if tecla not in self.botones_activos:
                keyboard.press(tecla)
                self.botones_activos.add(tecla)

                nombres = {
                    "z": "BOTÓN A",
                    "x": "BOTÓN B",
                    "enter": "START",
                    "backspace": "SELECT"
                }
                self.txt_botones.setHtml(f"<center><span style='font-size: 36pt;'>{nombres[tecla]}</span></center>")

        elif line.endswith("_UP"):
            base = line.replace("_UP", "")
            if base in botones:
                tecla = botones[base]
                if tecla in self.botones_activos:
                    keyboard.release(tecla)
                    self.botones_activos.discard(tecla)
                    self.txt_botones.clear()

        def closeEvent(self, event):
            self.detener_lector_serial()
            if self.arduino and self.arduino.is_open:
                self.arduino.close()
            event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
