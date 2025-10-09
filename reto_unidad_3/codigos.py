import math # ayuda de chat para poder definir la formula con la raiz cuadrada
#def = ayuda de ia para definir formulas de manera mas sencilla 

import math

opcion = "Z"

# 🔹 Historial global para la opción 3
historial_global = []

while opcion != "S":
    opcion = input(
        "1. Calcular velocidad mínima de aterrizaje\n"
        "2. Consumo de combustible en vuelo\n"
        "3. Sustentación en despegue\n"
        "4. Ver historial de sustentaciones\n"
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
                        print("⚠️ Velocidad alta: considere reducir peso antes del aterrizaje.")

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
                        print("⚠️ Fase inválida, no se consumió combustible")
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
                def calcular_sustentacion(rho, v, Cl, A):
                    return 0.5 * rho * (v**2) * Cl * A

                print("\n--- SIMULACIÓN: Sustentación en Despegue ---")

                avion = {
                    "peso": float(input("Peso del avión (N): ")),
                    "rho": float(input("Densidad del aire (kg/m3): ")),
                    "Cl": float(input("Coeficiente de sustentación: ")),
                    "A": float(input("Área alar (m2): ")),
                    "v": float(input("Velocidad inicial (m/s): ")),
                    "aceleracion": float(input("Aceleración en pista (m/s2): "))
                }

                # 🔹 Listas de registro para esta simulación
                velocidades = []
                sustentaciones = []

                while True:
                    avion["v"] += avion["aceleracion"]
                    L = calcular_sustentacion(avion["rho"], avion["v"], avion["Cl"], avion["A"])

                    velocidades.append(avion["v"])
                    sustentaciones.append(L)

                    print(f"Velocidad = {avion['v']:.2f} m/s | Sustentación = {L:.2f} N")

                    if L >= avion["peso"]:
                        print("\n ¡El avión alcanzó la sustentación suficiente y despegó!\n")
                        break

                # Guardar datos en el historial global
                historial_global.append({
                    "parametros": avion,
                    "velocidades": velocidades,
                    "sustentaciones": sustentaciones
                })

                print("✈️  Simulación de sustentación guardada correctamente.")

            # ------------------------------------------------------
            case "4":
                if len(historial_global) == 0:
                    print("\n No hay simulaciones guardadas aún.")
                else:
                    print("\n--- HISTORIAL DE SUSTENTACIONES ---")
                    for i, vuelo in enumerate(historial_global, start=1):
                        datos = vuelo["parametros"]
                        print(f"\nSimulación #{i}:")
                        print(f"  Peso: {datos['peso']} N | Cl: {datos['Cl']} | Área: {datos['A']} m²")
                        print(f"  Velocidades registradas: {vuelo['velocidades']}")
                        print(f"  Sustentaciones registradas: {vuelo['sustentaciones']}")

            # ------------------------------------------------------
            case _:
                print("\n Opción no válida.")

print("\nPrograma finalizado.")
