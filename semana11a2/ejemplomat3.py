import matplotlib.pyplot as plt
import numpy as np

#Muestra de 50 personas
categorias = ["Cine","Restaurante","Playa"]
hombres = [15,5,10]
mujeres = [12,8,5]

x = np.arange(len(categorias))

plt.bar(x-0.2,hombres,width=0.4,label="Hombres")
plt.bar(x+0.2,mujeres,width=0.4,label="Mujeres")
plt.xticks(x,categorias)
plt.title("¿Donde prefieres ir en una tarde con tu pareja?")
plt.legend()
plt.show()

