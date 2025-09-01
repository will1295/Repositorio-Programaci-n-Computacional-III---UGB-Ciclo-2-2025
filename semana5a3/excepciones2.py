class DivisionCero(Exception):
    def __init__(self, mensaje = "No puedes dividir entre cero"):
        super().__init__(mensaje)

def division(n1,n2):
    if n2 == 0:
        raise DivisionCero
    return n1/n2

n1 = int(input("Escribe un numero: "))
n2 = int(input("Escribe otro numero: "))
print(division(n1,n2))