
# --- Lectura 1: Objetos, Variables y Etiquetas ---
altitud = 10000          # metros
elevacion = altitud      # otra etiqueta apunta al mismo objeto
elevacion = 9500         # ahora elevacion apunta a un nuevo objeto
print("Altitud:", altitud)       # 10000
print("Elevación:", elevacion)   # 9500

# Conclusión:
# En Python las variables son solo nombres que apuntan a un valor.
# Cuando cambié elevacion = 9500, no cambió el 10000, solo moví la etiqueta a otro número.


# --- Lectura 2: ID de Objetos ---
velocidad = 800
print("ID velocidad:", id(velocidad))

otra_velocidad = 800
print("ID otra_velocidad:", id(otra_velocidad))

lista1 = [1, 3, 67]
print("ID lista1:", id(lista1))

# Conclusión:
# Cada valor tiene un ID propio.
# A veces dos números pequeños comparten ID porque Python los reutiliza.
# Las listas siempre tienen un ID distinto aunque tengan los mismos datos.


# --- Lectura 3: Mutabilidad vs Inmutabilidad ---
# Inmutable (string)
modelo = "Boeing 747"
print("ID modelo original:", id(modelo))
modelo = modelo + "-800"
print("Modelo modificado:", modelo)
print("ID modelo modificado:", id(modelo))

# Mutable (lista)
componentes = ["alas", "fuselaje", "motores"]
print("ID lista original:", id(componentes))
componentes.append("tren de aterrizaje")
print("Lista modificada:", componentes)
print("ID lista modificada:", id(componentes))

# Conclusión:
# Los strings no se pueden cambiar: al sumar “-800” al modelo se creó un objeto nuevo.
# Las listas sí se modifican sin cambiar su ID, como cuando agregué el tren de aterrizaje.


# --- Paso de argumentos a función ---
def agregar_combustible(tanques, litros):
    tanques.append(litros)
    print(f"Combustible actualizado: {tanques}")

combustible_actual = [1000, 1200, 800]
agregar_combustible(combustible_actual, 500)
print("Lista combustible final:", combustible_actual)

# Conclusión:
# Si paso una lista a una función, esa función puede cambiarla y el cambio se queda, porque la lista es mutable.
# Con enteros o strings no pasa: se crea otro valor y el original no se toca.


# --- Iterables e Iteración ---
sensores = ["temperatura", "presión", "velocidad", "altitud", "combustible"]
for sensor in sensores:
    print(f"Comprobando sensor de {sensor}...")

altitudes = [0, 100, 500, 1000, 1500, 2000, 2200, 2500]
tiempo = 0
i = 0
while i < len(altitudes):
    print(f"Tiempo: {tiempo}s - Altitud: {altitudes[i]} metros")
    tiempo += 10
    i += 1

for i, etapa in enumerate(["despegue", "ascenso", "crucero", "descenso", "aterrizaje"]):
    print(f"Etapa {i+1}: {etapa}")

tiempos = [0, 10, 20, 30]
velocidades = [0, 200, 300, 320]
for t, v in zip(tiempos, velocidades):
    print(f"Tiempo: {t}s - Velocidad: {v} km/h")

# Fin de la Actividad 1
