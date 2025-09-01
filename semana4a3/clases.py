class vehiculo:
    #Atributos o propiedades
    color = ""
    transmision = ""
    modelo = ""
    serie = ""
    marca = ""
    tipo = ""
    ncilindros = 0
    torque = 0
    hp = 0
    year = 0
    #Metodos
    #Metodo constructor
    def __init__(self,clr,trn,mod,ser,marc,tip,ncili,tor,hp,year):
        self.color = clr
        self.transmision = trn
        self.modelo = mod
        self.serie = ser
        self.marca = marc
        self.tipo = tip
        self.ncilindros = ncili
        self.torque = tor
        self.hp = hp
        self.year = year


    def datos(self):
        print(f"El carro es de color {self.color}")


    def acelerar(self):
        print(f"El {self.marca} {self.modelo} {self.serie} ha acelerado")

    def frenar(self):
        pass

    def cmarcha(self):
        pass

    def girar(self,angulogiro):
        if(angulogiro>0):
            print("El carro ha girado a la derecha")
        elif(angulogiro<0):
            print("El carro ha girado a la izquierda")

#Inicializacion o instancia de objeto con nombre 'carro1'
carro1 = vehiculo("rojo","estandar","lancer","X",
                  "mitsubishi","sedan qp",8,150,50,2008)
carro2 = vehiculo("verde","estandar","lancer","X",
                  "mitsubishi","sedan qp",8,150,50,2018)
#Acceso a el metodo acelerar por medio de "."
carro1.acelerar()
giro = int(input("Cual es el angulo de giro?"))
carro1.girar(giro)
#Acceso a la propiedad color
carro1.datos()
carro2.datos()