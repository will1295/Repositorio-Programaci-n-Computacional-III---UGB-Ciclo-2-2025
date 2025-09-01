n1 = int(input("Escribe un numero: "))
n2 = int(input("Escribe otro numero: "))
n3 = int(input("Escribe un tercer numero: "))

if n1>n2 and n1>n3:
    print(f"El mayor es {n1}")
elif n2>n1 and n2>n3:
    print(f"El mayor es {n2}")
elif n3>n1 and n3>n2:
    print(f"El mayor es {n3}")
#elif n1==n2 or n2==n3 or n1==n3:
#    print("Al menos dos numeros son iguales")
elif n1==n2:
    print("El primer y segundo numero son iguales")
elif n1==n3:
    print("El primer y tercer numero son iguales")
elif n2==n3:
    print("El segundo y tercer numero son iguales")        
else:
    print("Los tres numeros son iguales")

#Evaluar cual es el numero mayor, el menor y el de en medio