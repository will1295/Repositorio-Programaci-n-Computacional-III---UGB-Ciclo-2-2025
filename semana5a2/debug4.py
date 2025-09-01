def concatenar(palabras):
    frase = ""
    for p in palabras:
        frase+=p+" "
    return frase

texto = ["Hola","Mundo","Python"]
print(concatenar(texto))