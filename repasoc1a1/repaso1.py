#Una veterinaria registra los animalitos que atienden a consulta
#de manera escrita en la cual tienen datos de cada uno 
#ademas de poder revisar la informacion para tener un mejor
#control. El dueño de la veterinaria quiere que este proceso
#sea más automatizado por lo cual requiere un programa que le permita
#introducir la información y poder consultarla en cualquier momento

class Mascota:
   
   # nombre = ""
   # tipo = ""
   # edad = ""
   # peso = ""
    listado = []

    def __init__(self,nom,tipo,edad,peso):
        self.nombre = nom
        self.tipo = tipo
        self.edad = edad
        self.peso = peso
        Mascota.listado.append(self)

    def datos(self):
        for i,mascota in enumerate(Mascota.listado,1):
            print(f"{i} - Nombre: {mascota.nombre}\n"+
                  f"Tipo: {mascota.tipo}\n"+
                  f"Edad: {mascota.edad} años\n"+
                  f"Peso: {mascota.peso} libras\n")

# objeto datos de mascota = [(nombre=firulais,tipo=perro,edad=10,peso=20)]

mascota1 = Mascota("Firulais","Perro",10,20)
mascota2 = Mascota("Michi","Gato",5,10)
#mascota1.listado.append(mascota1)
mascota1.datos()