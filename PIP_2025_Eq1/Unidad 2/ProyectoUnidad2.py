import sys
import random
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "ProyectoUnidad02.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.carta_oculta = ":/ejercicios/Atras.jpg"
        self.imagenes = [
             ":/ejercicios/mariogold.jpeg", ":/ejercicios/cat.jpeg",
             ":/ejercicios/elyochi.jpg", ":/ejercicios/duolingo.jpeg",
             ":/ejercicios/wero.jpg"
        ] * 2

        random.shuffle(self.imagenes)

        self.labels = [
            self.lbl_img1, self.lbl_img2, self.lbl_img3, self.lbl_img4, self.lbl_img5,
            self.lbl_img6, self.lbl_img7, self.lbl_img8, self.lbl_img9, self.lbl_img10
        ]
        self.cartas_seleccionadas = []
        self.estado_cartas = [False] * len(self.labels)
        self.asignar_cartas_ocultas()
        self.habilitar_cartas(False)

        for i, label in enumerate(self.labels):
            label.mousePressEvent = lambda event, idx=i: self.voltear_carta(idx)

        self.btn_iniciar.clicked.connect(self.iniciar_juego)
        self.btn_reiniciar.clicked.connect(self.reiniciar_juego)
        self.btn_reiniciar.setEnabled(False)
        self.tiempo_restante = 30  # Segundos totales
        self.timer_juego = QtCore.QTimer()
        self.timer_juego.timeout.connect(self.actualizar_tiempo)
        self.lb_Tiempo.setText(str(self.tiempo_restante))
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.ocultar_cartas)

    def asignar_cartas_ocultas(self):
        for label in self.labels:
            label.setPixmap(QtGui.QPixmap(self.carta_oculta))
            label.setScaledContents(True)

    def habilitar_cartas(self, estado):
        for label in self.labels:
            label.setEnabled(estado)

    def voltear_carta(self, index):
        if len(self.cartas_seleccionadas) >= 2 or self.estado_cartas[index]:
            return

        self.labels[index].setPixmap(QtGui.QPixmap(self.imagenes[index]))
        self.labels[index].setScaledContents(True)
        self.cartas_seleccionadas.append(index)

        if len(self.cartas_seleccionadas) == 2:
            self.timer.start(1000)

    def ocultar_cartas(self):
        self.timer.stop()
        i, j = self.cartas_seleccionadas
        if self.imagenes[i] == self.imagenes[j]:
            self.estado_cartas[i] = self.estado_cartas[j] = True
        else:
            self.labels[i].setPixmap(QtGui.QPixmap(self.carta_oculta))
            self.labels[j].setPixmap(QtGui.QPixmap(self.carta_oculta))
            self.estado_cartas[i] = self.estado_cartas[j] = False

        self.cartas_seleccionadas = []

        if all(self.estado_cartas):
            self.juego_terminado()

    def juego_terminado(self):
        self.timer_juego.stop()
        self.habilitar_cartas(False)
        QtWidgets.QMessageBox.information(self, "¡Felicidades!", "¡Has ganado el juego!")
        self.btn_iniciar.setEnabled(False)
        self.btn_reiniciar.setEnabled(True)

    def iniciar_juego(self):
        random.shuffle(self.imagenes)
        self.asignar_cartas_ocultas()
        self.estado_cartas = [False] * len(self.labels)
        self.cartas_seleccionadas = []
        self.habilitar_cartas(True)
        self.btn_iniciar.setEnabled(False)
        self.btn_reiniciar.setEnabled(True)
        self.tiempo_restante = 30
        self.timer_juego.start(1000)
        self.actualizar_tiempo()

    def actualizar_tiempo(self):
        self.tiempo_restante -= 1
        self.lb_Tiempo.setText(str(self.tiempo_restante))
        if all(self.estado_cartas):
            return

        if self.tiempo_restante <= 0:
            self.timer_juego.stop()
            self.habilitar_cartas(False)
            QtWidgets.QMessageBox.information(self, "Fin del Tiempo", "¡Se acabó el tiempo! Intenta de nuevo.")
            self.reiniciar_juego()

    def reiniciar_juego(self):
        random.shuffle(self.imagenes)
        self.asignar_cartas_ocultas()
        self.estado_cartas = [False] * len(self.labels)
        self.cartas_seleccionadas = []
        self.habilitar_cartas(False)
        self.btn_iniciar.setEnabled(True)
        self.btn_reiniciar.setEnabled(False)
        self.timer_juego.stop()
        self.tiempo_restante = 30
        self.lb_Tiempo.setText(str(self.tiempo_restante))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
