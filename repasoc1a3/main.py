from repaso1 import Mascota
from repaso2 import Vehiculo,Carro,Moto

mascota1 = Mascota("Michi","Gato",2,10)
mascota2 = Mascota("Firulais","Perro",3,30)
#mascota1.mostrar_registros()
print(mascota1.get_nombre())
mascota1.set_nombre("Michito")
print(mascota1.get_nombre())

carro1 = Carro("Toyota","Corolla",5)
print(carro1.info())
moto1 = Moto("Marca aqui","Modelo aqui",500)
print(moto1.info())
