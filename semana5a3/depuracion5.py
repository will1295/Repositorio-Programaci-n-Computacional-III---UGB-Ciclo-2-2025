def buscar_num(lista,valor):
    for n in lista:
        if n == valor:
            return True
    return False

numeros = [3,7,9,10,11,20,44]
print(buscar_num(numeros,4))

