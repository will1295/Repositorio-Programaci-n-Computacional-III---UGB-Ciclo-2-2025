estudiante = {"nombre":"juan","apellido":"perez","edad":20,}

print(estudiante)
print(f"Mi nombre es {estudiante['nombre']} {estudiante['apellido']}")

datos = {
    "info":[
    ["juan","perez",20],
    ["maria","hernandez",19]
    ]
}
print(datos["info"][0][0])

libros = {
    "autor1":{"nombre":"ejemplo1","apellido":"apellido1","libro":"Un buen libro"},
    "autor2":{"nombre":"ejemplo2","apellido":"apellido2","libro":"Un gran libro"}
}

print(libros["autor1"]["nombre"])