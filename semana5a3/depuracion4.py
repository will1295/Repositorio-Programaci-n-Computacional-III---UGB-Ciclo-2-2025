def pares(numeros):
    npares = []
    for n in numeros:
        if n % 2 != 1:
            npares.append(n)
    return npares

valores = [3,6,9,10,24,2,68,11,44]
print(pares(valores))