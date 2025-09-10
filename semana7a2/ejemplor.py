import random
import time

print("***Juego de Monopoly***\n")
print("Primera ronda\n")

print(f"El primer jugador tira sus dados y obtiene:"+
      f"{random.randint(1,6)} y {random.randint(1,6)}\n")
print(f"El segundo jugador tira sus dados y obtiene:"+
      f"{random.randint(1,6)} y {random.randint(1,6)}\n")
print(f"El tercer jugador tira sus dados y obtiene:"+
      f"{random.randint(1,6)} y {random.randint(1,6)}\n")
print(f"El cuarto jugador tira sus dados y obtiene:"+
      f"{random.randint(1,6)} y {random.randint(1,6)}\n")


print("***Juego de Tirar la moneda***\n")

lado = ["cara","cruz"]

print("Primer jugador: \n")
print(f"Primer lanzamiento: {random.choice(lado)}\n")
time.sleep(5)
print(f"Segundo lanzamiento: {random.choice(lado)}\n")
time.sleep(5)
print(f"Tercer lanzamiento: {random.choice(lado)}\n")

print("Segundo jugador: \n")
time.sleep(5)
print(f"Primer lanzamiento: {random.choice(lado)}\n")
time.sleep(5)
print(f"Segundo lanzamiento: {random.choice(lado)}\n")
time.sleep(5)
print(f"Tercer lanzamiento: {random.choice(lado)}\n")

print("Tercer jugador: \n")
time.sleep(5)
print(f"Primer lanzamiento: {random.choice(lado)}\n")
time.sleep(5)
print(f"Segundo lanzamiento: {random.choice(lado)}\n")
time.sleep(5)
print(f"Tercer lanzamiento: {random.choice(lado)}\n")

#print(f"El segundo jugador tira las monedas y obtiene:"+
#      f"{random.choice(lado)} {random.choice(lado)} {random.choice(lado)}\n")
#print(f"El tercer jugador tira las monedas y obtiene:"+
#      f"{random.choice(lado)} {random.choice(lado)} {random.choice(lado)}\n")
#print(f"El cuarto jugador tira las monedas y obtiene:"+
#      f"{random.choice(lado)} {random.choice(lado)} {random.choice(lado)}\n")