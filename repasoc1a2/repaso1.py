#Una veterinaria ha llevado los registro de las mascotas hasta el
#momento a mano, el propietario de dicha vetarinaria quisiera
#que este proceso fuese mas automatizado por lo que 
#necesitaria un programa que le ayude con esta tarea y que ademas
#le permita revisar la informacion a los veterinarios
#acerca de cada uno de los pacientes

class Mascota:
    #nombre = ""
    #tipo = ""
    #edad = ""
    listado = []
    def __init__(self,nombre,tipo,edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.listado.append(self)
    
    def mostrar_datos(self):
        for i,mascota in enumerate(Mascota.listado,1):
            print(f"{i} - Nombre: {mascota.nombre} "+
                f"Tipo: {mascota.tipo} Edad: {mascota.edad} años")
                
    def info_mascota(self,nombre):
        for m in self.listado:
            if m.nombre == nombre:
                print("***Datos de la mascota***"+
                      f"Nombre: {self.nombre}"+
                      f"Tipo: {self.tipo}"+
                      f"Edad: {self.edad} años")
                



