import matplotlib.pyplot as plt

#Encuesta pasada a estudiantes universitarios
#acerca de la distribucion de sus gastos de manera mensual

categorias = ["Alimentacion","Transporte","Ocio","Ahorros"]
porcentajes = [50,30,15,5]

plt.pie(
    porcentajes,
    labels=categorias,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

plt.title("Distribucion de gastos de estudiantes universitarios")
plt.show()