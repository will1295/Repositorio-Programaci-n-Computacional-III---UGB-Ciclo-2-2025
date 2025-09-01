for i in range(5):
    print(f"{i+1} - Hello world!")

frutas = ["manzanas","peras","uvas"]

contador = 1
print("Lista de compras: ")
for f in frutas:
    print(f"{contador} - {f}")
    contador+=1

lista = []  
while True:
    nombre = input("Escribe un nombre: ")
    lista.append(nombre)
    op = input("Desea escribir otro nombre? (s/n)")
    if(op == "n"):
        break
print(lista)


#Crear una lista o tupla con 5 nombres  de personas
#Imprimir en pantalla cada uno de los nombres 
#completamente en mayusculas y que lleven un asterisco
#al comienzo de la impresion