import sys
import random
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap

qtCreatorFile = "E01_PiedraPapelTijeras.ui"  # Nombre del archivo UI
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class PiedraPapelTijeras(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #Area de los signals
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(2)
        self.imagenes = [":/ejercicios/Piedra.jpg", ":/ejercicios/Papel.jpg", ":/ejercicios/Tijeras.jpg"]
        self.nombres = ["Piedra", "Papel", "Tijeras"]
        self.ultima_eleccion = None
        self.horizontalSlider.valueChanged.connect(self.actualizar_imagen)
        self.btn_Jugar.clicked.connect(self.jugar)
        self.actualizar_imagen()


    # Area de los slots
    def actualizar_imagen(self):
        jugador = self.horizontalSlider.value()
        self.lbl_img1.setPixmap(QPixmap(self.imagenes[jugador]))
        self.lbl_img1.setScaledContents(True)

    def jugar(self):
        jugador = self.horizontalSlider.value()
        computadora = random.choice([0, 1, 2])
        self.ultima_eleccion = computadora

        # Actualiza la imagen de lbl_img1 (jugador) y lbl_img2 (computadora)
        self.lbl_img1.setPixmap(QPixmap(self.imagenes[jugador]))
        self.lbl_img1.setScaledContents(True)
        self.lbl_img2.setPixmap(QPixmap(self.imagenes[computadora]))
        self.lbl_img2.setScaledContents(True)


        # verificamos quien ganó el juego
        if jugador == computadora:
            resultado = "¡Empate (UnU)!"
        elif (jugador == 0 and computadora == 2) or (jugador == 1 and computadora == 0) or (
                jugador == 2 and computadora == 1):
            resultado = "¡Ganaste! :)"
        else:
            resultado = "Perdiste :("

        self.lbl_Resultado.setText(f"La PC eligió: {self.nombres[computadora]}\n{resultado}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = PiedraPapelTijeras()
    ventana.show()
    sys.exit(app.exec_())