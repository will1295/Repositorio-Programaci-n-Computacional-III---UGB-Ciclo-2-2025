#import PyQt5
from PyQt5.QtWidgets import (QApplication,QLabel,QWidget,
                             QPushButton,QVBoxLayout,QLineEdit,
                             QMessageBox)
import sys

def mensaje():
    texto = entradat.text()
    QMessageBox.information(ventana,"Mensaje",texto)

app = QApplication(sys.argv)
ventana = QWidget()
#Propiedades de una ventana
ventana.setWindowTitle("Mi primera ventana")
ventana.setGeometry(100,100,300,200)
layout = QVBoxLayout()
label = QLabel("Este un texto")
entradat = QLineEdit()
boton = QPushButton("Haz click aqui!")
boton.clicked.connect(mensaje)
layout.addWidget(label)
layout.addWidget(entradat)
layout.addWidget(boton)
ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())