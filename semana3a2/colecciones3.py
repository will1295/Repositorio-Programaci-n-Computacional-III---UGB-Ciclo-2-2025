listado = ["azul","morado","verde","rojo","amarillo"]
listado.append("negro")
print(listado)

listado.insert(2,"blanco")
print(listado)

listado.remove("morado")
print(listado)

listado.pop(1)
print(listado)

print(len(listado))

listado.sort()
print(listado)

listado2 = [34,12,7,45,2,10,91,120]
listado2.sort()
print(listado2)

print(listado2.index(12))
print(listado.index("verde"))