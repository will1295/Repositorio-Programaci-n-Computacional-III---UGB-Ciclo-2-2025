import matplotlib.pyplot as plt

categorias = ["Alimentacion","Transporte","Ocio","Ahorros"]
porcentajes = [40,30,25,5]

plt.pie(
    porcentajes,
    labels=categorias,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

plt.title("Distribucion de gastos de estudiantes universitarios al mes")
plt.show()