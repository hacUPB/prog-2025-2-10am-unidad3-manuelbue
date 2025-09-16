1.

```
Algoritmo VelocidadMinimaAterrizaje
    Definir función calcular_velocidad_aterrizaje(W, W_ref, V_ref):
        Retornar V_ref * sqrt(W / W_ref)

    Leer V_ref  // Velocidad de referencia
    Leer W_ref  // Peso de referencia

    Mientras verdadero hacer
        Leer W_actual
        V_landing ← calcular_velocidad_aterrizaje(W_actual, W_ref, V_ref)

        Escribir "Peso actual:", W_actual
        Escribir "Velocidad mínima de aterrizaje:", V_landing

        Si V_landing > 150 Entonces
            Escribir "Advertencia: Velocidad alta, considere reducir peso."
        FinSi

        Leer continuar
        Si continuar ≠ "Si" Entonces
            Escribir "Simulación terminada"
            Salir
        FinSi
    FinMientras
Fin
```


2.


``` 
inicio
Algoritmo ConsumoCombustible
    Definir combustible

    Definir función consumir_combustible(fase, tiempo):
        Si fase = 1 Entonces tasa ← 5
        Si fase = 2 Entonces tasa ← 3
        Si fase = 3 Entonces tasa ← 2
        Si fase no válido Entonces tasa ← 0
        combustible ← combustible - (tasa * tiempo)

    Leer combustible inicial

    Mientras combustible > 0 hacer
        Escribir "1. Ascenso | 2. Crucero | 3. Descenso"
        Leer fase
        Leer tiempo

        Llamar consumir_combustible(fase, tiempo)

        Si combustible > 0 Entonces
            Escribir "Combustible restante:", combustible
            Leer continuar
            Si continuar ≠ "Si" Entonces
                Salir
            FinSi
        Sino
            Escribir "¡Se acabó el combustible!"
            Salir
        FinSi
    FinMientras
Fin
```



3. 

``` 

Algoritmo SustentacionDespegue
    Definir función calcular_sustentacion(rho, v, Cl, A):
        Retornar 0.5 * rho * v^2 * Cl * A

    Leer peso
    Leer rho
    Leer Cl
    Leer A
    Leer v
    Leer aceleracion

    Mientras verdadero hacer
        v ← v + aceleracion
        L ← calcular_sustentacion(rho, v, Cl, A)

        Escribir "Velocidad:", v, " Sustentación:", L

        Si L ≥ peso Entonces
            Escribir "El avión alcanzó la sustentación suficiente y despegó"
            Salir
        FinSi
    FinMientras
Fin
```
