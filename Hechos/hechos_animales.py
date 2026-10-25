# Universo animales
universo = {
    "mamiferos": {
        "LeonMarino": ["ViveEnAgua", "TieneAletas", "OrejasExternas", "DaLeche"],
        "Guepardo": ["ComeCarne", "ColorLeonado", "ManchasOscuras"],
        "Tigre": ["ComeCarne", "ColorLeonado", "RayasNegras"],
        "Jirafa": ["TienePezunas", "CuelloLargo", "ManchasOscuras"],
        "Cebra": ["TienePezunas", "RayasNegras"],
        "Foca": ["ViveEnAgua", "TieneAletas"]
    },

    "aves": {
        "Pinguino": ["Nada", "BlancoNegro"],
        "Albatros": ["VuelaMuyBien"],
        "Pato": ["PatasPalmeadas", "PicoAnchoPlano", "CuelloCorto"],
        "Ganso": ["PatasPalmeadas", "CuelloLargo", "CuerpoGrande"]
    }
}

# Tuplas / Hechos
hechos = {

    ("LeonMarino", "vive", "Agua"),
    ("LeonMarino", "tiene", "Aletas"),
    ("LeonMarino", "tiene", "OrejasExternas"),

    ("Foca", "vive", "Agua"),
    ("Foca", "tiene", "Aletas"),

    ("Guepardo", "come", "Carne"),
    ("Guepardo", "tiene", "ManchasOscuras"),

    ("Tigre", "come", "Carne"),
    ("Tigre", "tiene", "RayasNegras"),

    ("Jirafa", "tiene", "CuelloLargo"),

    ("Cebra", "tiene", "RayasNegras"),

    ("Pinguino", "nada", "Si"),

    ("Albatros", "vuela", "MuyBien"),

    ("Pato", "tiene", "PatasPalmeadas"),

    ("Ganso", "tiene", "CuelloLargo")
}

# Predicados
def mamifero(x):
    for nombre in universo["mamiferos"]:
        if nombre == x:
            return True
    return False

def ave(x):
    for nombre in universo["aves"]:
        if nombre == x:
            return True
    return False

def carnivoro(x):
    if x == "Guepardo":
        return True

    if x == "Tigre":
        return True

    return False

def ungulado(x):
    if x == "Jirafa":
        return True

    if x == "Cebra":
        return True

    return False

def guepardo(x):
    if x == "Guepardo":
        return True
    return False

def tigre(x):
    if x == "Tigre":
        return True
    return False

def jirafa(x):
    if x == "Jirafa":
        return True
    return False

def cebra(x):
    if x == "Cebra":
        return True
    return False

def pinguino(x):
    if x == "Pinguino":
        return True
    return False

def albatros(x):
    if x == "Albatros":
        return True
    return False

def leon_marino(x):
    if x == "LeonMarino":
        return True
    return False

def foca(x):
    if x == "Foca":
        return True
    return False

def pato(x):
    if x == "Pato":
        return True
    return False

def ganso(x):
    if x == "Ganso":
        return True
    return False

# Consultas
print("1. Mamifero(Guepardo):", mamifero("Guepardo"))
print("2. Mamifero(Pato):", mamifero("Pato"))

print("3. Ave(Pinguino):", ave("Pinguino"))
print("4. Ave(Jirafa):", ave("Jirafa"))

print("5. Carnivoro(Tigre):", carnivoro("Tigre"))
print("6. Carnivoro(Cebra):", carnivoro("Cebra"))

print("7. Ungulado(Jirafa):", ungulado("Jirafa"))
print("8. Ungulado(Pinguino):", ungulado("Pinguino"))

print("9. Guepardo(Guepardo):", guepardo("Guepardo"))
print("10. Guepardo(Tigre):", guepardo("Tigre"))

print("11. Tigre(Tigre):", tigre("Tigre"))
print("12. Tigre(Cebra):", tigre("Cebra"))

print("13. Jirafa(Jirafa):", jirafa("Jirafa"))
print("14. Jirafa(Ganso):", jirafa("Ganso"))

print("15. Cebra(Cebra):", cebra("Cebra"))
print("16. Cebra(Pato):", cebra("Pato"))

print("17. Pinguino(Pinguino):", pinguino("Pinguino"))
print("18. Pinguino(Albatros):", pinguino("Albatros"))
