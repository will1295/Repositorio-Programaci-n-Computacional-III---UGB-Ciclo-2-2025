estudiante = {"nombre":"juan","apellido":"perez","edad":20}
print(f"Mi nombre es {estudiante["nombre"]} {estudiante["apellido"]}")

datos = {"estudiantes":[[
    "juan","perez",20,"san miguel"
],[
    "maria","hernandez",19,"usulutan"
]
],
"profesores":[
   ["mario","sanchez",40],
   ["andrea","ramirez",41] 
]
}
print(f"Profesor: {datos["profesores"][0][0]} {datos["profesores"][0][1]}")

datos2 = {
    "asignaturas":
    {
        "nombre":"matematica computacional",
        "duracion":"20 semanas",
        "cupo":30,
        "horario":"vespertino"        
    }
}

print(datos2["asignaturas"]["nombre"])