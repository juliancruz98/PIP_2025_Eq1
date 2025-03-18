import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E02_RelojAlarma.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Area de los signals
        self.btn_inicio.clicked.connect(self.establecer_alarma)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.verificar_alarma)

    #Area de los slots
    def establecer_alarma(self):
        if self.timer.isActive():
            self.timer.stop()
        try:
            horas = int(self.horas.text()) if self.horas.text() else 0
            minutos = int(self.minutos.text()) if self.minutos.text() else 0
            segundos = int(self.segundos.text()) if self.segundos.text() else 0
            self.alarma_tiempo = QtCore.QTime.currentTime().addSecs(horas * 3600 + minutos * 60 + segundos)
            self.timer.start(1000)
            self.btn_inicio.setText("Reiniciar")
        except ValueError:
            self.msj("Por favor, ingrese un tiempo válido.")

    def verificar_alarma(self):
        tiempo_restante = QtCore.QTime.currentTime().secsTo(self.alarma_tiempo)
        if tiempo_restante <= -1:
            self.timer.stop()
            self.msj("¡La alarma está sonando!")
            self.btn_inicio.setText("Empezar")
        else:
            self.pasado.setText(f"{tiempo_restante} segundos")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())