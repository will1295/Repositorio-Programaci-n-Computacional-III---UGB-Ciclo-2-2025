while True:
    try:
        n1 = int(input("Escribe un numero: "))
        n2 = int(input("Escribe otro numero: "))
        print(n1+n2)
    except:
        print("Valor invalido por favor ingrese un número")
    finally:
        op = input("Desea ejecutar el programa de nuevo? (s/n)")
        if(op == "n"):
            break
    