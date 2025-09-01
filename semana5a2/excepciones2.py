class divisioncero(Exception):
    def __init__(self, mensaje = "No puedes dividir entre cero!"):
        super().__init__(mensaje)

def dividir(n1,n2):
    if n2 == 0:
        raise divisioncero
    return n1/n2

print(dividir(10,0))