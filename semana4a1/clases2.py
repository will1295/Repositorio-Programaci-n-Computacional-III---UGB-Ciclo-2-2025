class Persona:

    #atributo
    sexo = ""
    edad = ""
    nombre = ""
    altura = ""

    def __init__(self,sexo,edad,nombre,altura):
        self.sexo = sexo
        self.edad = edad
        self.nombre = nombre
        self.altura = altura

    #metodo
    def comer(self):
        return "La persona esta comiendo"

    def dormir(self):
        print("La persona esta durmiendo")

class Empleado(Persona):

    salario = 0.0
    cargo = ""

    def __init__(self, sexo, edad, nombre, altura,salario,cargo):
        super().__init__(sexo, edad, nombre, altura)
        self.salario = salario
        self.cargo = cargo

    def trabajar(self):
        print("El empleado esta trabajando")

    def comer(self,comida):
        print(f"{super().comer()} {comida}") 
    

    def marcar(self,tipo):
        print(f"El empleado marcó {tipo}")

persona1 = Persona("M",20,"Juan",1.72)
persona1.comer()
empleado1 = Empleado("F",45,"Maria",1.63,500,"Directora")
empleado1.marcar("Entrada")
empleado1.trabajar()
empleado1.comer("Pollo guisado")
empleado1.trabajar()
empleado1.marcar("Salida")