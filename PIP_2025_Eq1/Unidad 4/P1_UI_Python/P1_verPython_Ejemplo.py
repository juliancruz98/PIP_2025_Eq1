from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 852)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(29, 183, 230);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imagen = QtWidgets.QLabel(self.centralwidget)
        self.imagen.setGeometry(QtCore.QRect(10, 20, 191, 161))
        self.imagen.setStyleSheet("")
        self.imagen.setText("")
        self.imagen.setPixmap(QtGui.QPixmap(":/ejercicios/elyochi.jpg"))
        self.imagen.setScaledContents(True)
        self.imagen.setObjectName("imagen")
        self.imagen_2 = QtWidgets.QLabel(self.centralwidget)
        self.imagen_2.setGeometry(QtCore.QRect(280, 30, 191, 161))
        self.imagen_2.setStyleSheet("")
        self.imagen_2.setText("")
        self.imagen_2.setPixmap(QtGui.QPixmap(":/ejercicios/kaldo.jpg"))
        self.imagen_2.setScaledContents(True)
        self.imagen_2.setObjectName("imagen_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(610, 10, 421, 341))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/ejercicios/samsgoku.jpeg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.txt_numero1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_numero1.setGeometry(QtCore.QRect(300, 410, 151, 61))
        self.txt_numero1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_numero1.setObjectName("txt_numero1")
        self.txt_numero2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_numero2.setGeometry(QtCore.QRect(300, 510, 151, 61))
        self.txt_numero2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_numero2.setObjectName("txt_numero2")
        self.btn_suma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_suma.setGeometry(QtCore.QRect(310, 690, 93, 28))
        self.btn_suma.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_suma.setObjectName("btn_suma")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 410, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 510, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1086, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_suma.setText(_translate("MainWindow", "SUMA"))
        self.label.setText(_translate("MainWindow", "NUMERO 1"))
        self.label_2.setText(_translate("MainWindow", "NUMERO 2"))
import Recursos_rc
