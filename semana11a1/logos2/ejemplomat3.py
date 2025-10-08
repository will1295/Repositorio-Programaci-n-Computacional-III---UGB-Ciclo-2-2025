import matplotlib.pyplot as plt
import numpy as np

#Muestra de 20 personas entre hombres y mujeres
#La encuesta trato de cual es lugar favorito para ir con tu pareja
#Opciones: Cine, Restaurante y Playa

categorias = ["Cine","Restaurante","Playa"]
hombres = [5,4,1]
mujeres = [2,5,3]

x = np.arange(len(categorias))
plt.bar(x-0.2,hombres,width=0.4,label="Hombres")
plt.bar(x+0.2,mujeres,width=0.4,label="Mujeres")
plt.xticks(x,categorias)
plt.legend()
plt.show()


