import matplotlib.pyplot as plt

x = [0,1,2,3,4,5]
y1 = [i**2 for i in x]
y2 = [i**3 for i in x]

plt.plot(x,y1,label="x**2",marker="o")
plt.plot(x,y2,label="x**3",marker="s")
plt.title("Comparacion de funciones")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()