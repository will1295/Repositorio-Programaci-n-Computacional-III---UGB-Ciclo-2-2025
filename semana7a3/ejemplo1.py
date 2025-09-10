import random

#print("Numero aleatorio entre cero y diez: ")
#print(random.randint(0,10))

print("***Juego de monopoly***\n")

print("Ronda 1\n")
print(f"Jugador 1 tira el dado y avanza {random.randint(1,6)} casillas\n")
print(f"Jugador 2 tira el dado y avanza {random.randint(1,6)} casillas\n")
print(f"Jugador 3 tira el dado y avanza {random.randint(1,6)} casillas\n")
print(f"Jugador 4 tira el dado y avanza {random.randint(1,6)} casillas\n")

print("***Juego de monedas***\n")
print("Hay cuatro personas y tiraran una moneda tres veces")

lado = ["cara","cruz"]

print("Ronda 1\n")
print(f"Jugador 1 tira sus monedas: {random.choice(lado)} {random.choice(lado)} {random.choice(lado)} \n")
print(f"Jugador 2 tira sus monedas: {random.choice(lado)} {random.choice(lado)} {random.choice(lado)} \n")
print(f"Jugador 3 tira sus monedas: {random.choice(lado)} {random.choice(lado)} {random.choice(lado)} \n")
print(f"Jugador 4 tira sus monedas: {random.choice(lado)} {random.choice(lado)} {random.choice(lado)} \n")
