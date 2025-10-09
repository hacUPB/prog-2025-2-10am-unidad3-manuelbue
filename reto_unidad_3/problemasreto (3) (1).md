# Situaciones Reto
1. Velocidad Mínima de Aterrizaje.
2. Consumo de combustible durante el vuelo (según fases y duración).
3. Cálculo de sustentación en despegue (simulación hasta alcanzar velocidad mínima de vuelo).

# PLANTEAMIENTO DE CADA PROBLEMA
## Opción 1: 
-**Contexto:** En la aviación, la velocidad mínima de aterrizaje depende directamente del peso actual del avión. A medida que el avión consume combustible y su peso disminuye, la velocidad de aterrizaje también cambia.

-**Objetivo:** Simular en vuelo la variación de la velocidad mínima de aterrizaje según el peso actual del avión, comparando con un valor de referencia.

-**Relevancia:** Calcular correctamente la velocidad mínima de aterrizaje es esencial para garantizar la seguridad durante la aproximación y el aterrizaje, evitando velocidades excesivas que comprometan la operación.

**Elementos del programa:**

-**Bucle:** el usuario puede ingresar diferentes valores de peso actual mientras dure la simulación.

-**Condicionales:** el programa advierte si la velocidad de aterrizaje supera un límite seguro (150 nudos).

-**Función:** calcular_velocidad_aterrizaje(W, W_ref, V_ref), que ajusta la velocidad mínima de aterrizaje según el peso actual en relación con el peso de referencia.
## Opción 2: Consumo de Combustible en Vuelo
-**Contexto:** 
el avión consume combustible a diferentes tasas dependiendo de la fase
del vuelo (ascenso, crucero, descenso).

-**Objetivo:** 
Simular un vuelo donde el usuario selecciona la fase y la duración de cada
segmento, calculando cuánto combustible queda.

-**Relevancia:** 
Controlar el combustible es vital en aeronáutica para la planificación del
vuelo.

**Elementos:**

-**Bucle:** 
el usuario va agregando fases hasta quedarse sin combustible o
terminar el vuelo.

-**Condicionales:** 
consumo varía según la fase.

-**Función:** 
resta de combustible por fase.
## Opción 3: Sustentación en Despegue
**Contexto:** Un avión necesita alcanzar cierta velocidad mínima (stall speed) para
generar suficiente sustentación y despegar.

**Objetivo:** Simular la carrera de despegue, donde la velocidad aumenta cada segundo
hasta que la sustentación supera al peso.

**Relevancia:** Es clave en operaciones de despegue y seguridad aeronáutica.

**Elementos:**

-**Bucle:** segundo a segundo se incrementa la velocidad.

-**Condicionales:** verificar si ya se alcanzó la sustentación suficiente.

-**Función:** cálculo de la sustentación.
