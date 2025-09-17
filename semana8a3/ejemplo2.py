#import PyQt5
from PyQt5.QtWidgets import (QApplication,QWidget,
                             QPushButton,QVBoxLayout,QLabel,QLineEdit,
                             QMessageBox)
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)

def mensaje():
    n1 = float(entrada1.text())
    n2 = float(entrada2.text())
    QMessageBox.information(ventana,"Mensaje",f"La suma es: {n1+n2}")

ventana = QWidget()
ventana.setWindowTitle("Suma de dos numeros")
ventana.setGeometry(300,300,500,200)
icono = QIcon("python.ico")
ventana.setWindowIcon(icono)
layout = QVBoxLayout()
texto = QLabel("Esto es un texto")
entrada1 = QLineEdit()
entrada2 = QLineEdit()
boton1 = QPushButton("Haz click aqui!")
boton1.clicked.connect(mensaje)
#layout.addWidget(texto)
#layout.addWidget(entrada1)
#layout.addWidget(entrada2)
#layout.addWidget(boton1)
widgets = [texto,entrada1,entrada2,boton1]
for w in widgets:
    layout.addWidget(w)
ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())