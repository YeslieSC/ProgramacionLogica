# Universo de la universidad
universo = {
    "estudiantes": {
        "Yeslie": ["ProgramacionLogica", "Investigacion", "Ecuaciones"],
        "Juan": ["Investigacion", "Ecuaciones"]
    },
    "profesores": {
        "Carlos": ["ProgramacionLogica", "Ecuaciones"],
        "Juana": ["Investigacion", "Tutor"]
    },
    "lugares": ["Biblioteca", "Cafeteria"]

# Predicados
}
def estudiante(x):
    for nombre in universo["estudiantes"]:
        if nombre == x:
            return True
    return False
def profesor(y):
    for nombre in universo["profesores"]:
        if nombre == y:
            return True
    return False
def materia(m):
    materias = ["ProgramacionLogica", "Investigacion", "Ecuaciones"]
    return m in materias
def inscrito(x, m):
    if x in universo["estudiantes"]:
        return m in universo["estudiantes"][x]
    return False
def aprueba(x, m):
    if x == "Yeslie":
        return m in universo["estudiantes"][x]
    if x == "Juan":
        return m == "Ecuaciones"
    return False
def reprueba(x, m):
    if x == "Juan" and m == "Investigacion":
        return True
    return False
def asiste(x, m):
    if x == "Yeslie" and m == "ProgramacionLogica":
        return True
    if x == "Juan" and m == "Ecuaciones":
        return True
    return False

# Consultas
print("1. Estudiante(Yeslie):", estudiante("Yeslie"))
print("2. Estudiante(Carlos):", estudiante("Carlos"))

print("3. Profesor(Carlos):", profesor("Carlos"))
print("4. Profesor(Yeslie):", profesor("Yeslie"))

print("5. Materia(ProgramacionLogica):", materia("ProgramacionLogica"))
print("6. Materia(Cafeteria):", materia("Cafeteria"))

print("7. Inscrito(Yeslie, Investigacion):", inscrito("Yeslie", "Investigacion"))
print("8. Inscrito(Juan, ProgramacionLogica):", inscrito("Juan", "ProgramacionLogica"))

print("9. Aprueba(Yeslie, Ecuaciones):", aprueba("Yeslie", "Ecuaciones"))
print("10. Aprueba(Juan, Investigacion):", aprueba("Juan", "Investigacion"))

print("11. Reprueba(Juan, Investigacion):", reprueba("Juan", "Investigacion"))
print("12. Reprueba(Yeslie, Ecuaciones):", reprueba("Yeslie", "Ecuaciones"))

print("13. Asiste(Juan, Ecuaciones):", asiste("Juan", "Ecuaciones"))
print("14. Asiste(Juan, ProgramacionLogica):", asiste("Juan", "ProgramacionLogica"))

