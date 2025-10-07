import matplotlib.pyplot as plt

calificaciones = [6.5,7.2,7.5,8,8.2,8.5,8.7,8.8,9,9.1,9.2,9.4,9.5,9.7,9.8,10,6.5,7,7.8]

plt.hist(
    calificaciones,
    bins=9,
    range=(1,10),
    color="#255C42",
    edgecolor="black"
)

plt.title("Distribucion de calificaciones")
plt.xlabel("Rango de calificaciones")
plt.ylabel("Numero de estudiantes")

plt.show()