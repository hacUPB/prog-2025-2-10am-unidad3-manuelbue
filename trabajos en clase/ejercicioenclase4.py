def menu():
    print("1. entradas\n2. platos fuertes\n3. Bebidas\n4. postres\nS. salida")
    opcion = int(input("elija una opcion:"))
    return opcion

def entradas():
    print("1. pan de bono\t\t $3000")
    print("2. empanada\t\t $3500")

def fuertes():
    print("1. mojarra a la francesa\t\t $80000")
    print("2. pasta venezolana\t\t $45000")

def bebidas():
    print("1. jugo de carambolo\t\t $15000")
    print("2. jugo de borojó\t\t $15000")

def postres():
    print("1. chocolatico con pan\t\t $20000")
    print("2. helado de borojo\t\t $12000")
# Funcion principal
eleccion = menu()
print(eleccion)
3
match(eleccion):
    case 1:
        entradas()
    case 2:
        fuertes()
    case 3:
        bebidas()
    case 4:
        postres()
    case _:
        print("opcion no valida")