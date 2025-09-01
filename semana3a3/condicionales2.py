contador = 0

while contador <= 10:
    print("Hello world!")
    contador+=1

while True:
    print("Hello world!")
    op = input("Desea salir del bucle? (s/n)")
    if(op == 's'):
        break

num = 0
while num <=10:
    num+=1
    if num % 2 == 0:
        continue
    print(num)
   
#Pedir numeros al usuario
#Si el usuario da un numero positivo mostrar el doble
#Si el usuario da un numero negativo ignorar el codigo
#Si el usuario ingresa 0 se sale del programa
