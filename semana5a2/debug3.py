def buscar_numero(lista,valor):
    breakpoint()
    for n in lista:
        if n!=valor:
            return True
    return False

numeros = [2,4,8,10,12,20,24]
print(buscar_numero(numeros,5))