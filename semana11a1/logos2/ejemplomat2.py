import matplotlib.pyplot as plt

x = [0,1,2,3,4,5]
cuadrados = [0,1,4,9,16,25]
cubos = [0,1,8,27,64,125]

plt.plot(x,cuadrados,label="Cuadrados",marker="o")
plt.plot(x,cubos,label="Cubos",marker="s")
plt.title("Comparacion de funciones")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()