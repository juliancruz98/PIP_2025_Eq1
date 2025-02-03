import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E12_PromedioNumeros_Load.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.btn_cargar.clicked.connect(self.cargar)
        self.calificaciones = []
        self.cargas=0

    #Area de los slots
    def cargar(self):
        #archivo=open   
        # TAREA como compruebo si el archivo existe #ejercicio 10
        if self.cargas>=1:
            self.msj("No puedes cargar otro archivo")
            return

        archivo = open("../../Archivos/calificaciones.csv")
        contenido = archivo.readlines()
        print(contenido)
        datos =[int(x)for x in contenido]
        print(datos)
        self.calificaciones = datos
        self.cargas+=1

        #11 en lugar de sobrescribir concatenar
        #12 asegurarse de que solo se pueda cargar hasta antes de agregar la primera califiaciones

    def agregar(self): #ta bien
        calificacion = int(self.txt_calificacion.text())
        self.calificaciones.append(calificacion)
        self.promedio()

    def promedio (self): #ta bien
        prom = sum(self.calificaciones)/len(self.calificaciones)
        self.txt_promedio.setText(str(prom))

    def guardar(self): #ta bien
        archivo=open("../../Archivos/calificaciones.csv", "w")
        for c in self.calificaciones:
            archivo.write(str(c)+'\n')
        archivo.flush()
        archivo.close()
        self.msj("Archivo guardado con exito!!!")


    def msj(self,txt):
        m=QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())