import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton
                             ,QVBoxLayout,QHBoxLayout,QGridLayout,
                             QFormLayout,QRadioButton,QLabel,
                             QComboBox,QLineEdit,QSpinBox,
                             QDoubleSpinBox,QMessageBox)

app = QApplication(sys.argv)

def mensaje():
    QMessageBox.information(ventana,"Alerta","Hiciste click!")
    
ventana = QWidget()
layout = QVBoxLayout()
ventana.setWindowTitle("Mi primera ventana con pyqt5")
ventana.setGeometry(200,200,600,400)
label1 = QLabel("Esto es un label")
edit1 = QLineEdit()
boton1 = QPushButton("Haz click aqui")
boton1.clicked.connect(mensaje)
radio1 = QRadioButton("Opcion 1")
radio2 = QRadioButton("Opcion 2")
radio3 = QRadioButton("Opcion 3")
combo1 = QComboBox()
combo1.addItem("Enero")
combo1.addItem("Febrero")
combo1.addItem("Marzo")
combo1.addItem("Abril")
spin1 = QSpinBox()
dspin1 = QDoubleSpinBox()
#layout.addWidget(label1)
#layout.addWidget(edit1)
#layout.addWidget(boton1)
#layout.addWidget(radio1)
#layout.addWidget(radio2)
#layout.addWidget(radio3)
#layout.addWidget(combo1)
#layout.addWidget(spin1)
#layout.addWidget(dspin1)
widgets = [label1,edit1,boton1,radio1,radio2,radio3,combo1,spin1,dspin1]
for w in widgets:
    layout.addWidget(w)

ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())