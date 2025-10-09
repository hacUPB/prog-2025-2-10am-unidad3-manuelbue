import math # ayuda de chat para poder definir la formula con la raiz cuadrada
#def = ayuda de ia para definir formulas de manera mas sencilla 

opcion = "Z"

# 🔹 Historial global para la opción 3
historial_global = []

while opcion != "S":
    opcion = input(
        "1. Calcular velocidad mínima de aterrizaje\n"
        "2. Consumo de combustible en vuelo\n"
        "3. Sustentación en despegue\n"
        "S. Salir\n"
        "Seleccione la opción que desea ejecutar: "
    ).upper()

    if opcion != "S":
        match opcion:
            # ------------------------------------------------------
            case "1":
                def calcular_velocidad_aterrizaje(W, W_ref, V_ref):
                    return V_ref * math.sqrt(W / W_ref)

                print("\n--- SIMULACIÓN: Velocidad mínima de aterrizaje ---")

                V_ref = float(input("Ingrese velocidad de referencia (nudos): "))
                W_ref = float(input("Ingrese peso de referencia (kg): "))

                while True:
                    W_actual = float(input("\nIngrese el peso actual del avión (kg): "))
                    V_landing = calcular_velocidad_aterrizaje(W_actual, W_ref, V_ref)

                    print(f"Peso actual: {W_actual:.0f} kg")
                    print(f"Velocidad mínima de aterrizaje: {V_landing:.2f} nudos")

                    if V_landing > 150:
                        print(" Velocidad alta: considere reducir peso antes del aterrizaje.")

                    continuar = input("¿Desea continuar la simulación? (Si/No): ").lower()
                    if continuar != "si":
                        print("Simulación terminada.")
                        break

            # ------------------------------------------------------
            case "2":
                combustible = 0

                def consumir_combustible(fase, tiempo):
                    global combustible
                    if fase == 1:
                        tasa = 5
                    elif fase == 2:
                        tasa = 3
                    elif fase == 3:
                        tasa = 2
                    else:
                        print(" Fase inválida, no se consumió combustible")
                        tasa = 0
                    combustible -= tasa * tiempo

                print("\n--- SIMULACIÓN: Consumo de combustible ---")
                combustible = float(input("Ingresar combustible inicial (L): "))

                while combustible > 0:
                    print("\nFases: 1. Ascenso | 2. Crucero | 3. Descenso")
                    fase = int(input("Seleccionar fase: "))
                    tiempo = int(input("Duración de la fase (min): "))

                    consumir_combustible(fase, tiempo)

                    if combustible > 0:
                        print(f"Combustible restante = {combustible:.2f} L")
                        continuar = input("¿Continuar vuelo? (Si/No): ").lower()
                        if continuar != "si":
                            break
                    else:
                        print("¡Se acabó el combustible en pleno vuelo!")
                        break

            # ------------------------------------------------------
            case "3":
                # Función para calcular sustentación
                def calcular_sustentacion(rho, v, Cl, A):
                    return 0.5 * rho * (v**2) * Cl * A

                # Variables iniciales
                historial = []
                salir_submenu = False

                while not salir_submenu:
                    print("\n--- MENÚ DE SUSTENTACIÓN EN DESPEGUE ---")
                    print("1. Ejecutar nueva simulación")
                    print("2. Ver historial de simulaciones")
                    print("3. Salir del programa")

                    subopcion = input("Seleccione una opción: ")

                    if subopcion == "1":
                        print("\n--- NUEVA SIMULACIÓN ---")

                        # Diccionario con los datos del avión
                        avion = {
                            "peso": float(input("Peso del avión (N): ")),
                            "rho": float(input("Densidad del aire (kg/m3): ")),
                            "Cl": float(input("Coeficiente de sustentación: ")),
                            "A": float(input("Área alar (m2): ")),
                            "v": float(input("Velocidad inicial (m/s): ")),
                            "aceleracion": float(input("Aceleración en pista (m/s2): ")) }

                        simulacion = []  # lista temporal para esta simulación

                        # Simulación segundo a segundo
                        while True:
                            avion["v"] += avion["aceleracion"]
                            L = calcular_sustentacion(avion["rho"], avion["v"], avion["Cl"], avion["A"])

                            registro = {"velocidad": avion["v"], "sustentacion": L}
                            simulacion.append(registro)

                            print(f"Velocidad = {avion['v']:.2f} m/s | Sustentación = {L:.2f} N")

                            if L >= avion["peso"]:
                                print("\nEl avión alcanzó la sustentación suficiente y despegó.\n")
                                break

                        historial.append(simulacion)

                        print("Resumen de la simulación:")
                        for i, paso in enumerate(simulacion, start=1):
                            print(f"t={i}s → V={paso['velocidad']:.2f} m/s | L={paso['sustentacion']:.2f} N")

                    elif subopcion == "2":
                        if len(historial) == 0:
                            print("\nNo hay simulaciones registradas todavía.\n")
                        else:
                            print("\n--- HISTORIAL DE SIMULACIONES ---")
                            for n, simulacion in enumerate(historial, start=1):
                                print(f"\nSimulación #{n}")
                                for i, paso in enumerate(simulacion, start=1):
                                    print(f"t={i}s → V={paso['velocidad']:.2f} m/s | L={paso['sustentacion']:.2f} N")

                    elif subopcion == "3":
                        print("\nCerrando el programa desde el submenú de sustentación...\n")
                        exit()  # termina el programa completamente

            case _:
                print("\n Opción no válida.")

print("\nPrograma finalizado.")
