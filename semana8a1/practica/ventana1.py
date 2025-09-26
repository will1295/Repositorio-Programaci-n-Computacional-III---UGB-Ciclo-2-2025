import sys
from PyQt5.QtWidgets import (QApplication,QWidget,
                             QVBoxLayout,QPushButton,
                             QLineEdit,QLabel,
                             QMessageBox)

app = QApplication(sys.argv)

def mensaje():
    info = entrada1.text()
    QMessageBox.information(ventana,
                            "Mensaje",info)

ventana = QWidget()
layout = QVBoxLayout()
label1 = QLabel("Esto es un texto")
boton1 = QPushButton("Haz click aqui!")
boton1.clicked.connect(mensaje)
entrada1 = QLineEdit()
layout.addWidget(label1)
layout.addWidget(boton1)
layout.addWidget(entrada1)
ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec())


#HACER UNA VENTANITA QUE PERMITA HACER
#LAS CUATRO OPERACIONES BASICAS CON DOS NUMEROS
