from random import randint,choice
from time import sleep
#randint genera un numero entero entre un rango de valores

print("***Juego de monopoly***")
print("***Ronda 1***")
print("***Turno jugador 1***")
print(f"El jugador tiro un dado y obtuvo: {randint(1,6)}")

print("***Turno jugador 2***")
print(f"El jugador tiro un dado y obtuvo: {randint(1,6)}")

print("***Turno jugador 3***")
print(f"El jugador tiro un dado y obtuvo: {randint(1,6)}")

print("***Turno jugador 4***")
print(f"El jugador tiro un dado y obtuvo: {randint(1,6)}")


lado = ["Cara","Cruz"]
print("***Juego de la moneda***")
print("***Turno jugador 1***")
print("El jugador tiro un tres monedas y obtuvo: ") 
print(f"{choice(lado)}")
sleep(3)
print(f"{choice(lado)}")
sleep(3)
print(f"{choice(lado)}")
sleep(1)
print("***Turno jugador 2***")
print("El jugador tiro un tres monedas y obtuvo: ") 
print(f"{choice(lado)}")
sleep(3)
print(f"{choice(lado)}")
sleep(3)
print(f"{choice(lado)}")
sleep(1)
print("***Turno jugador 3***")
print("El jugador tiro un tres monedas y obtuvo: ") 
print(f"{choice(lado)}")
sleep(3)
print(f"{choice(lado)}")
sleep(3)
print(f"{choice(lado)}")


