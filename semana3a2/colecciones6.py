persona = {"nombre":"juan","apellido":"perez","edad":20}

#print(persona["nombre"])

print(f"Hola mi nombre es {persona['nombre']} {persona['apellido']}")


estudiantes = {
    "estudiante1":[
        "juan","perez",20,"San Miguel"
    ]
}

print(estudiantes["estudiante1"][0])

datos = {
    "estudiantes":[
        ["maria","hernandez",19,"Morazan"],
        ["luis","martinez",21,"San Miguel"]
    ],
    "profesores":[
        ["juan","ramirez",41,"Usulutan"],
        ["antonio","gomez",39,"San Miguel"]
    ]
}

#Print que muestre en pantalla el nombre del profesor antonio gomez
print(f"{datos["profesores"][1][0]} {datos["profesores"][1][1]}")