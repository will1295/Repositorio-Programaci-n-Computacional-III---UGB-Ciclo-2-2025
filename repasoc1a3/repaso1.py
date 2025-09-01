#Una veterinaria ha crecido mucho en los ultimos años
#y hasta el momento se llevaba un registro de los pacientes
#a mano, entoces el propietario quiere llevar un mejor registro
#mas automatizado que le permita revisar la informacion de cada
#animalito cuando el lo requiera
class Mascota:
    #nombre = ""
    #especie = ""
    listado = []

    def __init__(self,nombre,especie,edad,peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso
        Mascota.listado.append(self)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre

    def mostrar_registros(self):
        for i,mascota in enumerate(Mascota.listado,1):
            print(f"{i}.Nombre de la mascota: {mascota.nombre} Especie: {mascota.especie}"+ 
                  f"Edad: {mascota.edad} Peso en lb: {mascota.peso}")
            
if __name__ == "__main__":
    pass
