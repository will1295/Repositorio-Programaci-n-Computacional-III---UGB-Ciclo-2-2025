num1 = input("Escribe un numero: ")
num2 = input("Escribe un numero: ")
num3 = input("Escribe un numero: ")

#Imprimir de los tres numeros cual es el mayor, el menor y 
# el del medio
if num1 > num2 and num1>num3:
    if num2>num3:
        print(f"El {num1} es mayor")
        print(f"El {num2} es es el del medio")
        print(f"El {num1} es el menor")
    
elif num2<num1:
    print(f"El {num2} es mayor")
else:
    print(f"Los numeros son iguales")