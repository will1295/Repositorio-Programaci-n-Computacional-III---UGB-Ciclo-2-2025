class carro:
    #aributos o propiedades
    modelo = ""
    year = 0
    color = ""
    capacidad = 0
    placa = ""

    #metodo constructor o inicializador de clase
    def __init__(self,mod,ye,col,cap):
        self.modelo = mod
        self.year = ye
        self.color = col
        self.capacidad = cap

    #metodos
    def transportar(self,origen,destino):
        print(f"Se hara un viaje de {origen} hasta {destino}")

    def acelerar(self):
        print("El carro ha acelerado")

    def enceder(self):
        print(f"El carro {self.modelo} ha encendido")

    def frenar(self):
        pass

    def estacionar(self):
        pass

    def registro(self,placa):
        self.placa = placa
        print(f"Placa del vehiculo: {self.placa}")

    def en_luces(self,valor):
        if(valor=="alta"):
            print("Has encendido las luces altas")
        elif(valor=="baja"):
            print("Has encendido las luces bajas")
        


#Instancias de clase u objetos
carro1 = carro("Tsubaru",2025,"Rosado",2)
carro1.enceder()
carro1.acelerar()
carro2 = carro("Toyota Corolla",2015,"Azul",5)
#carro2.modelo = "Sentra"
carro2.registro("P12KJHI")
carro2.enceder()
carro2.acelerar()
origen = input("Desde donde vas a viajar?")
dest = input("Hasta donde vas a viajar?")
valor = input("Que intensidad de luz vas a poner? (alta/baja)")
carro2.transportar(origen,dest)
carro2.en_luces(valor)
