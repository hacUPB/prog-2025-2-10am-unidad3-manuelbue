import math # ayuda de chat para poder definir la formula con la raiz cuadrada
#def = ayuda de ia para definir formulas de manera mas sencilla 

opcion = "Z"
while opcion != "S":
    opcion=input("1. calcula velocidad minima de aterrizaje \n2. consumo de combustible en vuelo\n3. sustentacion en despegue\nS. salir\n selecione la opcion que quiere ejecutar: ").upper()
    opcion =opcion.upper()
    if opcion != "S":
        match opcion:
            case "1":
                def calcular_velocidad_aterrizaje(W, W_ref, V_ref):# sqrt = raiz cuadrada

                    
                    return V_ref * math.sqrt(W / W_ref)

                print(" Simulación de Velocidad de Aterrizaje en Vuelo ")

                # Datos de referencia
                V_ref = float(input("Ingrese velocidad de referencia (nudos): "))
                W_ref = float(input("Ingrese peso de referencia (kg): "))

                # Bucle de vuelo
                while True:
                    W_actual = float(input("\nIngrese el peso actual del avión (kg): "))
                    
                    V_landing = calcular_velocidad_aterrizaje(W_actual, W_ref, V_ref)
                    
                    print(f"Peso actual: {W_actual:.0f} kg")
                    print(f"Velocidad mínima de aterrizaje: {V_landing:.2f} nudos")
                    
                    if V_landing > 150:
                        print(" Advertencia: Velocidad alta, considere reducir peso antes del aterrizaje.")
                    
                    continuar = input("¿Desea continuar la simulación en vuelo? (Si/No): ").lower()
                    if continuar != "Si":
                        print("Simulación terminada. ")
                        break
            case "2":
                  # Variable global de combustible
                    combustible = 0

                    def consumir_combustible(fase, tiempo):
                        global combustible   # accede a la variable global

                        # Seleccionar tasa de consumo según la fase
                        if fase == 1:      # Ascenso
                            tasa = 5       # L/min
                        elif fase == 2:    # Crucero
                            tasa = 3       # L/min
                        elif fase == 3:    # Descenso
                            tasa = 2       # L/min
                        else:
                            print(" Fase inválida, no se consumió combustible")
                            tasa = 0       # si fase inválida, no gasta combustible
                        
                        # Actualizar directamente la variable global
                        combustible = combustible - (tasa * tiempo)


                    # --- Algoritmo principal ---
                    print("\n--- PSEUDOCÓDIGO OPCIÓN 2: Consumo de Combustible ---")

                    combustible = float(input("Ingresar combustible inicial (L): "))

                    # Mientras haya combustible
                    while combustible > 0:
                        print("\nFases: 1. Ascenso | 2. Crucero | 3. Descenso")
                        fase = int(input("Seleccionar fase: "))
                        tiempo = int(input("Duración de la fase (min): "))

                        consumir_combustible(fase, tiempo)   # se actualiza la variable global

                        if combustible > 0:
                            print(f"Combustible restante = {combustible:.2f} L")
                            continuar = input("¿Continuar vuelo? (SI/No): ").lower()
                            if continuar != "Si":
                                break
                        else:
                            print("¡Se acabó el combustible en pleno vuelo!")
                            break
            case "3":
                def calcular_sustentacion(rho, v, Cl, A):
                    # Fórmula de la sustentación
                    L = 0.5 * rho * (v**2) * Cl * A
                    return L


                # --- Algoritmo principal ---
                print("\n--- PSEUDOCÓDIGO OPCIÓN 3: Sustentación en Despegue ---")

                peso = float(input("Peso del avión (N): "))
                rho = float(input("Densidad del aire (kg/m3): "))
                Cl = float(input("Coeficiente de sustentación: "))
                A = float(input("Área alar (m2): "))
                v = float(input("Velocidad inicial (m/s): "))
                aceleracion = float(input("Aceleración en pista (m/s2): "))

                # Simulación segundo a segundo
                while True:
                    v += aceleracion
                    L = calcular_sustentacion(rho, v, Cl, A)
                    print(f"Velocidad = {v:.2f} m/s | Sustentación = {L:.2f} N")

                    if L >= peso:
                        print("¡El avión alcanzó la sustentación suficiente y despegó!")
                        break
            case "S":
                  print("Saliendo del programa...")
            case _:
                print("opcion no valida")

