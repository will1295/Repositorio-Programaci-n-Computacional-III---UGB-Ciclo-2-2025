class vehiculo:
    #atributos o propiedades
    marca = ""
    color = ""
    tipo = ""
    year = 0
    transmision = ""

    #metodo constructor
    def __init__(self,marca,color,tipo,year,transmision):
        self.marca = marca
        self.color = color
        self.tipo = tipo
        self.year = year
        self.transmision = transmision

    #metodos
    def moverse(self):
        pass

    def transportar(self):
        pass

    def arrancar(self):
        print(f"El carro {self.marca} arrancó")

    def cvelocidad(self,cambio):
        if(self.transmision == "Manual"):
            if(cambio == 2):
                print("Pasamos a segunda")
            elif(cambio == 3):
                print("Pasamos a tercera")
        elif(self.transmision == "Automatica"):
            if(cambio == "D"):
                print("Se ha puesto en marcha")
            elif(cambio == "R"):
                print("Se esta retrocediendo")

carro1 = vehiculo("Nissan","Negro","Camioneta",2005,"Manual")
#carro1.marca = "Toyota"
carro1.arrancar()
carro1.cvelocidad(2)
carro1.cvelocidad(3)

carro2 = vehiculo("Chevrolet","Azul","Sedan",2007,"Automatica")
carro2.arrancar()
carro2.cvelocidad("D")
carro2.cvelocidad("R")