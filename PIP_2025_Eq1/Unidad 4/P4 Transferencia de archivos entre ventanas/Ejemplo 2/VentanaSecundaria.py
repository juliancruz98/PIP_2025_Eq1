
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile3 = "Second_RecepcionInfo.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)


class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self,  rPrincipal):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.acceso = rPrincipal

        self.btn_sumar.clicked.connect(self.sumar)


    # Área de los Slots
    def sumar(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())

        r = a + b
        print(r)

        self.acceso.txt_resultado.setText(str(r))

        self.close()