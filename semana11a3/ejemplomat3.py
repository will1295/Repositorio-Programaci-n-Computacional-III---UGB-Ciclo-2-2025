import matplotlib.pyplot as plt
import numpy as np

categorias = ["A","B","C"]
val1 = [4,7,1]
val2 = [6,3,8]

x = np.arange(len(categorias))

plt.bar(x-0.2,val1,width=0.4,label="Grupo 1")
plt.bar(x+0.2,val2,width=0.4,label="Grupo 2")
plt.xticks(x,categorias)
plt.legend()
plt.show()