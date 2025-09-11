Float (decimal) → Es un número con coma o punto decimal.

Ejemplo: 75.5, 0.98, 1200.0

Integer (entero) → Es un número sin decimales.

Ejemplo: 1, 300, -25

String (texto) → Es una palabra, frase o cualquier texto escrito entre comillas.

Ejemplo: "sí", "no", "opción 1", "menu principal"




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
