#import PyQt5
from PyQt5.QtWidgets import (QApplication,QWidget,
                             QPushButton,QVBoxLayout,QLabel,QLineEdit,
                             QMessageBox)
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)

def mensaje():
    textom = texto.text()
    QMessageBox.information(ventana,"Mensaje",textom)


ventana = QWidget()
ventana.setWindowTitle("Mi primer ventana con PyQt5")
ventana.setGeometry(300,300,500,200)
icono = QIcon("python.ico")
ventana.setWindowIcon(icono)
layout = QVBoxLayout()
texto = QLabel("Esto es un texto")
entrada = QLineEdit()
boton1 = QPushButton("Haz click aqui!")
boton1.clicked.connect(mensaje)
layout.addWidget(texto)
layout.addWidget(entrada)
layout.addWidget(boton1)
ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())