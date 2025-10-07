import matplotlib.pyplot as plt

categorias = ["Alimentacion","Transporte","Entretenimiento","Ahorros"]
porcentajes = [45,35,10,10]
colores = ["#7BF1A8","#8E51FF","#FFD230","#FFA1AD"]

plt.pie(
    porcentajes,
    labels=categorias,
    colors=colores,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

plt.title("Distribucion gastos de estudiantes universitarios")
plt.show()