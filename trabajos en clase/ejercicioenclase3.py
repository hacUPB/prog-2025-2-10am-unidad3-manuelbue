opcion = "Z"
while opcion != "Q":
    opcion=input("F. Farenheit a celsius \nC. Celsius a farenheit\nQ. salir\n selecione la opcion que quiere ejecutar: ").upper()
    opcion =opcion.upper()
    if opcion != "Q":
        temperatura = float(input("ingrese la temperatura a convertir: "))
        match opcion:
            case "F":
                conversion = ((temperatura -32)* (5/9))
                print(f"{temperatura}°F = {conversion}°C")
            case "C":
                conversion=((temperatura *(9/5))+32)
                print(f"{temperatura}°C = {conversion}°F")
            case "Q":
                print("Saliendo del programa...")
            case _:
                print("opcion no valida")
