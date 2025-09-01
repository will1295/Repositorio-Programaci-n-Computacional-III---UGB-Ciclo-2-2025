class persona:
    edad = 0
    altura = 0.0
    sexo = ""
    nombre = ""

    def __init__(self,edad,altura,sexo,nombre):
        self.edad = edad
        self.altura = altura
        self.sexo = sexo
        self.nombre = nombre

    def caminar(self):
        print(f"{self.nombre} esta caminando")

    def hablar(self):
        pass

    def comer(self):
        pass

class empleado(persona):
    cargo = ""
    sueldo = 0.0

    def __init__(self, edad, altura, sexo, nombre,cargo,sueldo):
        super().__init__(edad, altura, sexo, nombre)
        self.cargo = cargo
        self.sueldo = sueldo

    def laborar(self):
        print(f"{self.nombre} esta trabajando")

    def marcar(self,tipo,hora):
        print(f"Hora de {tipo}: {hora}")

    def info(self):
        print(f"Tengo el cargo de {self.cargo}")

class estudiante(persona):
    carrera=""
    carnet=""

    def __init__(self, edad, altura, sexo, nombre,carrera,carnet):
        super().__init__(edad, altura, sexo, nombre)
        self.carrera = carrera
        self.carnet = carnet

    def estudiar(self):
        print("Hora de estudiar..")

    def iralauni(self):
        pass


persona1 = persona(20,1.67,"F","Anita")
persona1.caminar()

empleado1 = empleado(49,1.72,"M","Pepito","Ordenanza",400)
empleado1.caminar()
empleado1.info()
empleado1.marcar("Entrada","8:05 a.m.")
empleado1.laborar()
empleado1.marcar("Salida","5.00 p.m.")


estudiante1=estudiante(20,1.73,"M","Juanito","Ing en sistemas","SMSSS12321")
estudiante1.caminar()
estudiante1.estudiar()