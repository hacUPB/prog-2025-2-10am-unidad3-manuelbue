# Situaciones Reto
1. Simulación de fuerza de arrastre (Drag dinámico con variación de velocidad).
2. Consumo de combustible durante el vuelo (según fases y duración).
3. Cálculo de sustentación en despegue (simulación hasta alcanzar velocidad mínima
de vuelo).
4. Salir del programa.

# ANÁLISIS DE CADA PROBLEMA
## Opción 1: Simulación de Fuerza de Arrastre (Drag)
• Contexto: La fuerza de arrastre depende de la velocidad, el área alar, la densidad del
aire y el coeficiente de arrastre.
• Objetivo: Simular durante varios segundos cómo cambia el arrastre mientras el
usuario decide aumentar, disminuir o mantener la velocidad.
• Relevancia: El arrastre limita la velocidad y el rendimiento del avión, fundamental en
aerodinámica.
• Elementos:
o Bucle: simula segundo a segundo el vuelo.
o Condicionales: decisiones del usuario sobre la velocidad.
o Función: cálculo del arrastre.
## Opción 2: Consumo de Combustible en Vuelo
• Contexto: El avión consume combustible a diferentes tasas dependiendo de la fase
del vuelo (ascenso, crucero, descenso).
• Objetivo: Simular un vuelo donde el usuario selecciona la fase y la duración de cada
segmento, calculando cuánto combustible queda.
• Relevancia: Controlar el combustible es vital en aeronáutica para la planificación del
vuelo.
• Elementos:
o Bucle: el usuario va agregando fases hasta quedarse sin combustible o
terminar el vuelo.
o Condicionales: consumo varía según la fase.
o Función: resta de combustible por fase.
## Opción 3: Sustentación en Despegue
• Contexto: Un avión necesita alcanzar cierta velocidad mínima (stall speed) para
generar suficiente sustentación y despegar.
• Objetivo: Simular la carrera de despegue, donde la velocidad aumenta cada segundo
hasta que la sustentación supera al peso.
• Relevancia: Es clave en operaciones de despegue y seguridad aeronáutica.
• Elementos:
o Bucle: segundo a segundo se incrementa la velocidad.
o Condicionales: verificar si ya se alcanzó la sustentación suficiente.
o Función: cálculo de la sustentación.
