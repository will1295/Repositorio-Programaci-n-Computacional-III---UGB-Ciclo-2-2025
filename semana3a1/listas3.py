lista = ["lapiz","lapicero","borrador","sacapunta","plumones"]

#index
print(lista.index("borrador"))
#append
lista.append("cuadernos")
print(lista)
#insert
lista.insert(2,"compás")
print(lista)
#remove
lista.remove("lapiz")
print(lista)
lista.pop(3)
print(lista)

#sort
lista2 = [4,23,8,1,50,100,20,42]
lista.sort()
lista2.sort()
lista[3]="lapiceros"
print(lista)
print(lista2)

#len
print(len(lista))
