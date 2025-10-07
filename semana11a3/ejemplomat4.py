import matplotlib.pyplot as plt
import numpy as np

categorias = ["Cine","Restaurante","Playa"]
#20 personas
hombres = [12,5,7]
mujeres = [8,15,13]

x = np.arange(len(categorias))

plt.bar(x-0.2,hombres,width=0.4,label="Hombres")
plt.bar(x+0.2,mujeres,width=0.4,label="Mujeres")
plt.xticks(x,categorias)
plt.title("Preferencia de lugar para una cita")
plt.legend()
plt.show()