n1=int(input("Escribe un numero: "))
n2=int(input("Escribe un numero: "))
n3=int(input("Escribe un numero: "))

#Mostrar el numero menor y el de en medio
if n1>n2 and n1>n3:
    if n2>n3:
        print(f"El mayor es: {n1}\n"+
              f"El menor es: {n3}\n"+
              f"El del medio es: {n2}\n")
    #print(f"El mayor es: {n1}")
elif n2>n1 and n2>n3:
    print(f"El mayor es {n2}")
elif n3>n1 and n3>n2:
    print(f"El mayor es {n3}")
