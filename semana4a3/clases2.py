class persona:
    nombre = ""
    apellido = ""
    edad = 0

    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def nombrecom(self):
        print(f"Mi nombre es: {self.nombre} {self.apellido}")

class empleado(persona):
    identificador = ""
    puesto = ""

    def __init__(self, nombre, apellido, edad,identificador,puesto):
        super().__init__(nombre, apellido, edad)
        self.identificador = identificador
        self.puesto = puesto

    def datos(self,salario):
        print(f"Tengo el puesto de {self.puesto} y gano ${salario} al mes")


persona1 = persona("pepito","perez",20)
persona1.nombrecom()
empleado1 = empleado("maria","hernandez",30,"ID1000","secretaria")
empleado1.nombrecom()
salario = input("¿Cuanto ganas al mes en dolares? ")
empleado1.datos(salario)
