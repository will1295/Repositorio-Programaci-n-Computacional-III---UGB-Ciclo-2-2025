for i in range(5):
    print("Hello world!")

lista1 = ["lapiz","borrador","sacapunta","lapicero"]
contador = 1

print("***Lista de utiles escolares***\n")
for elemento in lista1:
    print(f"{contador} - {elemento}\n")
    contador+=1


estudiantes = []
nombre = input("Ingresa el nombre del estudiante: ")
estudiantes.append(nombre)

#Pedir nombres de estudiantes y agregarlos a una lista
#hasta que el usuario decida detenerse
#y luego imprimirlos en pantalla uno por uno