#import PyQt5
from PyQt5.QtWidgets import (QApplication,QLabel,QWidget,
                             QPushButton,QVBoxLayout,QLineEdit,
                             QMessageBox)
import sys

def mensaje():
    n1 = float(enum1.text())
    n2 = float(enum2.text())
    resultado = n1+n2
    QMessageBox.information(ventana,"Resultado"
                            ,f"El resultado es: {resultado}")

app = QApplication(sys.argv)
ventana = QWidget()
#Propiedades de una ventana
ventana.setWindowTitle("Suma de dos numeros")
ventana.setGeometry(100,100,300,200)
layout = QVBoxLayout()
label = QLabel("Ingresa dos numeros y sumalos")
enum1 = QLineEdit()
enum2 = QLineEdit()
boton = QPushButton("Sumar")
boton.clicked.connect(mensaje)
#layout.addWidget(label)
#layout.addWidget(enum1)
#layout.addWidget(enum2)
#layout.addWidget(boton)

widgets = [label,enum1,enum2,boton]
for w in widgets:
    layout.addWidget(w)

ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())