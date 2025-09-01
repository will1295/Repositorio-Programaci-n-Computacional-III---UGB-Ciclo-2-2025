def promedio(lista):
    #breakpoint()
    suma = 0
    for n in lista:
        suma = n+suma
    return suma/len(lista)
print(promedio([5,12,10,20,25,8]))