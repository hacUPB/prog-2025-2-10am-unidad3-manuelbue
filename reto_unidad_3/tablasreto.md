Float (decimal) → Es un número con coma o punto decimal.

Ejemplo: 75.5, 0.98, 1200.0

Integer (entero) → Es un número sin decimales.

Ejemplo: 1, 300, -25

String (texto) → Es una palabra, frase o cualquier texto escrito entre comillas.

Ejemplo: "sí", "no", "opción 1", "menu principal"


## variables de control


1. Velocidad mínima de aterrizaje

W_actual → variable que cambia en cada iteración y determina el cálculo de la velocidad mínima.

continuar → controla si el bucle Mientras sigue ejecutándose o se detiene.

Condicional: Si V_landing > 150 → controla la alerta de advertencia.

2. Consumo de combustible en vuelo

combustible → variable principal que controla si el bucle sigue (combustible > 0).

fase → define la tasa de consumo (controla el cálculo en cada ciclo).

tiempo → controla cuánto combustible se resta en cada fase.

continuar → controla si el usuario quiere seguir en el bucle o salir.

3. Sustentación en despegue

v (velocidad) → aumenta en cada iteración y controla el crecimiento de la sustentación.

L (sustentación) → se compara con el peso para detener el bucle.

Condicional: Si L ≥ peso → condición de salida del bucle (el avión despega).




### Caso 1: Velocidad Mínima de Aterrizaje  

| Variable     | Tipo de Dato (Entrada/Salida/Constante) | Explicación |
|--------------|-----------------------------------------|------------|
| **V_ref**    | Float – Entrada/Constante | Velocidad de aterrizaje de referencia. El usuario la pone al inicio y después queda fija. |
| **W_ref**    | Float – Entrada/Constante | Peso de referencia del avión, que corresponde a V_ref. Se da al inicio y luego no cambia. |
| **W_actual** | Float – Entrada   | El peso actual del avión. Este valor lo mete el usuario en cada repetición del bucle. |
| **V_landing**| Float – Salida    | La velocidad mínima de aterrizaje que calcula el sistema usando V_ref y W_actual. |
| **opcion**   | String – Entrada  | Opción que elige el usuario en el menú principal. |
| **continuar**| String – Entrada  | Sirve para que el usuario diga si quiere seguir con la simulación o no. |

---

### Caso 2: Consumo de Combustible en Vuelo  

| Variable     | Tipo de Dato (Entrada/Salida/Constante) | Explicación |
|--------------|-----------------------------------------|------------|
| **combustible** | Float – Entrada/Salida | El combustible que queda en el tanque: empieza con un valor que pone el usuario y se va restando en cada fase de vuelo. |
| **fase**     | Integer – Entrada       | Indica la parte del vuelo (1 = Ascenso, 2 = Crucero, 3 = Descenso). De esto depende el consumo. |
| **tiempo**   | Integer – Entrada       | Cuánto dura la fase en minutos. Se usa para calcular el consumo de combustible. |
| **tasa**     | Integer – Constante     | La cantidad de combustible que se gasta por minuto, depende de la fase de vuelo. |
| **opcion**   | String – Entrada        | Opción que elige el usuario en el menú principal. |
| **continuar**| String – Entrada        | El usuario responde si quiere seguir con la simulación o detenerla. |

---

### Caso 3: Sustentación en Despegue  

| Variable     | Tipo de Dato (Entrada/Salida/Constante) | Explicación |
|--------------|-----------------------------------------|------------|
| **peso**     | Float – Entrada       | El peso del avión. Para despegar, la sustentación debe ser mayor que este valor. |
| **rho**      | Float – Constante     | La densidad del aire, un dato fijo en la fórmula de sustentación. |
| **Cl**       | Float – Constante     | El coeficiente de sustentación. Depende del diseño del ala y el ángulo de ataque. |
| **A**        | Float – Constante     | El área del ala del avión. |
| **v**        | Float – Entrada       | La velocidad del avión, que va aumentando mientras acelera en la pista. |
| **aceleracion** | Float – Constante  | La aceleración del avión en la pista, sirve para ir aumentando la velocidad en cada paso. |
| **L**        | Float – Salida        | La fuerza de sustentación que se calcula con la fórmula: \(L = \tfrac{1}{2}\rho v^2 Cl A\). |
| **opcion**   | String – Entrada      | Opción que elige el usuario en el menú principal. |



Ayuda IA
| Reto                           | Ecuación principal                                      | Variables involucradas |
|--------------------------------|---------------------------------------------------------|-------------------------|
| 1. Velocidad mínima de aterrizaje | \( V_{landing} = V_{ref} \cdot \sqrt{\tfrac{W}{W_{ref}}} \) | \(V_{landing}\): velocidad mínima de aterrizaje<br>\(V_{ref}\): velocidad de referencia<br>\(W\): peso actual<br>\(W_{ref}\): peso de referencia |
| 2. Consumo de combustible       | \( Combustible = Combustible - (tasa \cdot tiempo) \)   | \(Combustible\): litros disponibles<br>\(tasa\): consumo según fase (5, 3 o 2 L/min)<br>\(tiempo\): duración de la fase (min) |
| 3. Sustentación en despegue     | \( L = \tfrac{1}{2} \cdot \rho \cdot v^2 \cdot C_L \cdot A \) <br> Condición: \(L \geq Peso\) | \(L\): sustentación<br>\(\rho\): densidad del aire<br>\(v\): velocidad<br>\(C_L\): coeficiente de sustentación<br>\(A\): superficie alar<br>\(Peso\): peso del avión |