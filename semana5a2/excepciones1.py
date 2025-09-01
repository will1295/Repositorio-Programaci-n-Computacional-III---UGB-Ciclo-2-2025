while True:
    try:
        n1 = int(input("Escribe un numero: "))
        n2= int(input("Escribe un numero: "))
        print(n1+n2)
    except:
        print("Por favor ingrese un número valido")
    finally:
        op = input("Desea ejecutar de nuevo el programa? (s/n)")
        if (op == "n"):
            break
