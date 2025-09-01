contador = 1

while contador <= 5:
    print("Hello world!")
    contador +=1


while True:
    nom = input("Escribe un nombre")
    print(f"Hola {nom} pasa buen dia")
    op = input("Desea continuar? (s/n)")
    if(op=='n'):
        break

num = 0

while num < 10:
    num +=1
    if num %2 ==0:
        continue
    print(f"Numero impar: {num}")


#Pedir al usuario numeros hasta que se ingrese 0, si 
#se ingresa 0 el programa debe detenerse
#si se ingresa un numero positivo debe mostrarse el doble del valor
#si se ingresa un numero negativo debe ignorarse