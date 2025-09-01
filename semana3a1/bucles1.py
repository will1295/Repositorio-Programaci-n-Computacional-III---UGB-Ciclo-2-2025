"""
contador = 1
while contador<10:
    print("Hello world!")
    #contador=contador+1
    contador+=1
    
while True:
    nombre = input("Escribe tu nombre!")
    print(f"Buenos dias {nombre}")
    op = input("Deseas salir del programa? (s/n)")
    if op == "s":
        break
"""
contador = 0
while contador<=15:
    contador+=1
    if contador%2 == 0:
        continue
    print(contador)
#Evaluar la entrada de un usuario de la siguiente forma:
# Si el usuario ingresar un numero positivo imprimir su doble
# Si el usuario ingresar un numero negativo omitirlo
# Si el usuario ingresa cero detener el programa    
