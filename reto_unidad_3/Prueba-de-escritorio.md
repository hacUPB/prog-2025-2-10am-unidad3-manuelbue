# PRUEBA DE ESCRITORIO:
## Algoritmo 1 Velocidad Minima Aterrizaje
# Prueba de escritorio

## Datos iniciales
- V_ref = 120  
- W_ref = 100000  
- Iteración 1: W_actual = 90000  
- Iteración 2: W_actual = 160000  
- continuar = "Si" en la primera vuelta, luego "No"

---

## Tabla

| Paso | Instrucción / Acción | Variables (V_ref, W_ref, W_actual, V_landing, continuar) | Salida / Observación |
|------|-----------------------|----------------------------------------------------------|-----------------------|
| 1    | Leer V_ref            | V_ref=120, W_ref=?, W_actual=?, V_landing=?, continuar=? | — |
| 2    | Leer W_ref            | V_ref=120, W_ref=100000, W_actual=?, V_landing=?, continuar=? | — |
| 3    | Leer W_actual         | V_ref=120, W_ref=100000, W_actual=90000, V_landing=?, continuar=? | — |
| 4    | Calcular V_landing    | V_landing = 120 * sqrt(90000/100000) = 113.84            | — |
| 5    | Escribir resultados   | V_ref=120, W_ref=100000, W_actual=90000, V_landing=113.84 | Muestra: Peso=90000, Velocidad=113.84 |
| 6    | Condición V>150       | 113.84 > 150 → Falso                                     | No hay advertencia |
| 7    | Leer continuar        | continuar="Si"                                           | Sigue el bucle |
| 8    | Leer W_actual         | V_ref=120, W_ref=100000, W_actual=160000                 | — |
| 9    | Calcular V_landing    | V_landing = 120 * sqrt(160000/100000) = 151.79           | — |
| 10   | Escribir resultados   | V_ref=120, W_ref=100000, W_actual=160000, V_landing=151.79 | Muestra: Peso=160000, Velocidad=151.79 |
| 11   | Condición V>150       | 151.79 > 150 → Verdadero                                 | Muestra advertencia |
| 12   | Leer continuar        | continuar="No"                                           | Termina bucle |
| 13   | Escribir mensaje final | —                                                        | "Simulación terminada" |


#### NOTA: se solicitó una pequeña asesoría de la iA para organizar la información en tabla.

De esta prueba de escritorio pudimos concluir que:
1. El pseudocódigo tiene estructura clara: definición de función, lectura de datos, ciclo, operaciones y condicionales. 

2. La fórmula V_ref * sqrt(W / W_ref) está bien aplicada y da resultados numéricamente correctos. 

3. El flujo de control (mientras verdadero + condición de salida) funciona porque depende de la variable continuar. 

4. Los mensajes de salida corresponden con los cálculos hechos. 
5. Para W_actual = 90000 obtuvimos 113.84, que es razonable (menor que la referencia porque el peso bajó).

6. Para W_actual = 160000 obtuvimos 151.79, mayor a la referencia, y el algoritmo correctamente detectó la condición y mostró la advertencia
