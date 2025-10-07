import matplotlib.pyplot as plt

x = [0,1,2,3,4,5]
y1 = [0,1,4,9,16,25]
y2 = [0,1,8,27,64,125]

plt.plot(x,y1,label="Cuadrados",marker="o")
plt.plot(x,y2,label="Cubos",marker="s")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()