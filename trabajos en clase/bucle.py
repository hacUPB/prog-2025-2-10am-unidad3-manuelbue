while True:
    num1 = int(input("ingresa un numero entero: "))
    num2 = int(input("ingresa otro numero entero: "))
    print("S, sumar\nR, Restar\nM, Multiplicar\nD, Dividir\nP, Potencia\nE, salir")
    opcion= input("elija una opcion: ")
    opcion = opcion.upper()
    match opcion:
        case "S":
            print("suma")
            resultado = num1 + num2
        case "R":
            print("resta")
            resultado = num1 - num2
        case "M":
            print("multiplicacion")
            resultado = num1 * num2
        case "D":
            if num2 == 0 :
                print("no se puede dividir")
            else: 
                print("Division")
                resultado = num1 / num2
        case "P":
            print("Potenciacion")
            resultado = num1 ** num2
        case "E":
            break
        case _:
            print("opcion invalida")
    print(f"resultado = {resultado}")