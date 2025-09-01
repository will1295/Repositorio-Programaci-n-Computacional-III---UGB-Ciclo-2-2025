#En un autolote se rentan diferentes tipo de vehiculos,
#dependiendo del vehiculo la tarifa de renta cambia
#cada vehiculo se registra y tambien se muestra los datos
#respectivamente

class Vehiculo:

    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        
    def info(self):
        return f"{self.marca} {self.modelo}"
    
    def cobro(self,dias,tarifa):
        return dias*tarifa
    

class Carro(Vehiculo):
    def __init__(self, marca, modelo,pasajeros):
        super().__init__(marca, modelo)
        self.pasajeros = pasajeros

    def info(self):
        return f"{super().info()} Cantidad de pasajeros: {self.pasajeros}"
    
    def cobro(self,dias,tarifa):
        precio_base = 20
        if self.pasajeros>4:
            precio_base +=20
        print(f"Precio de renta: {precio_base+(dias*tarifa)}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo,cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje

    def info(self):
        return f"{super().info()} Cilindraje: {self.cilindraje}"
    
    def cobro(self,dias,tarifa):
        seguro_accidentes = 30
        print(f"Precio de renta: {seguro_accidentes+(dias*tarifa)}")



      
