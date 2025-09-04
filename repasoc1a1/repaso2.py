#Un negocio de renta de carros lleva contratos escritos acerca de
#las rentas que los clientes solicitan, el cual contiene datos
#del vehiculo, el tiempo de renta, costos adiciones y tarifa
#El dueño del negocio necesita que esto sea más agil por medio
#de un sistema que le permita hacer los cobros de manera mas eficiente

class Vehiculo:

    def __init__(self,tarifa,tiempo):
        self.tarifa = tarifa
        self.tiempo = tiempo

    def cobro(self):
        return self.tarifa*self.tiempo
    
class Carro(Vehiculo):

    def __init__(self, tarifa, tiempo,marca,modelo,placa,personas):
        super().__init__(tarifa, tiempo)
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.personas = personas

    def cobro(self):
        return super().cobro()+(self.personas*5)


class Moto(Vehiculo):

    def __init__(self, tarifa, tiempo,marca,modelo,placa,seguro):
        super().__init__(tarifa, tiempo)
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.seguro = seguro

    def cobro(self):
        if(self.seguro==True):
            return super().cobro()+50
        else:
            return super().cobro()

class Microbus(Vehiculo):

    def __init__(self, tarifa, tiempo,marca,modelo,placa,destino):
        super().__init__(tarifa, tiempo)
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.destino = destino

    def cobro(self):
        if(self.destino!="El Salvador"):
            return super().cobro()+100
        else:
            return super().cobro()
    
carro1 = Carro(30,5,"Toyota","Corrolla","P123SMA",2)
print(f"Total: ${carro1.cobro()}")
moto1 = Moto(25,3,"Yamaha","MT-03","M12JSD",False)
print(f"Total: ${moto1.cobro()}")
microbus1 = Microbus(50,3,"Patito","El mejor de todos","MB12JKAS","Guatemala")
print(f"Total: ${microbus1.cobro()}")