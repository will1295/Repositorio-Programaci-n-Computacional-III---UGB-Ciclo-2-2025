from repaso1 import Mascota
from repaso2 import Carro,Moto

#instancias de objetos
mascota1 = Mascota("Michi","Gato",2)
mascota2 = Mascota("Firulais","Perro",5)
mascota1.mostrar_datos()

mascota1.info_mascota("Michi")


carro1 = Carro("Toyota","Corolla",5)
print(carro1.info())
carro1.cobro(5,30)

moto1 = Moto("Honda","12CSAD",500)
print(moto1.info())
moto1.cobro(3,20)