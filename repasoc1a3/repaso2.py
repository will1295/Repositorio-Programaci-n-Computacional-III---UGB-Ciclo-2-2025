class Vehiculo:

    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def info(self):
        return f"{self.marca} {self.modelo}"
    
class Carro(Vehiculo):
    def __init__(self, marca, modelo,pasajeros):
        super().__init__(marca, modelo)
        self.pasajeros = pasajeros

    def info(self):
        return f"{super().info()} Pasajeros: {self.pasajeros}"
    
class Moto(Vehiculo):
    def __init__(self, marca, modelo,cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def info(self):
        return f"{super().info()} Pasajeros: {self.cilindrada}" 


if __name__ == "__main__":
    pass  
