### 📋 Caso 1: Velocidad Mínima de Aterrizaje  

| Variable     | Tipo de Dato (Entrada/Salida/Constante) | Comentario |
|--------------|-----------------------------------------|------------|
| **V_ref**    | Float – Entrada/Constante | Velocidad de aterrizaje de referencia. El usuario la proporciona al inicio y luego permanece fija durante la simulación. |
| **W_ref**    | Float – Entrada/Constante | Peso de referencia del avión, que corresponde a V_ref. Se ingresa al inicio y luego se mantiene constante. |
| **W_actual** | Float – Entrada   | El peso actual del avión. Este valor es variable y se ingresa en cada iteración del bucle. |
| **V_landing**| Float – Salida    | La velocidad mínima de aterrizaje calculada con la fórmula que ajusta V_ref según el peso actual. |
| **opcion**   | String – Entrada  | La entrada del usuario para seleccionar la opción del menú principal. |
| **continuar**| String – Entrada  | La entrada del usuario para decidir si continúa la simulación dentro del bucle. |




### 📋 Caso 2: Consumo de Combustible en Vuelo  

| Variable     | Tipo de Dato (Entrada/Salida/Constante) | Comentario |
|--------------|-----------------------------------------|------------|
| **combustible** | Float – Entrada/Salida | El combustible en el tanque: inicia con un valor dado por el usuario y se actualiza en cada fase de vuelo. |
| **fase**     | Integer – Entrada       | Representa la fase de vuelo (1 = Ascenso, 2 = Crucero, 3 = Descenso). Determina la tasa de consumo. |
| **tiempo**   | Integer – Entrada       | La duración de la fase de vuelo en minutos. Se usa para calcular el total de combustible consumido en esa fase. |
| **tasa**     | Integer – Constante     | La tasa de consumo de combustible, definida en la función según la fase de vuelo. |
| **opcion**   | String – Entrada        | La opción que selecciona el usuario en el menú principal. |
| **continuar**| String – Entrada        | La entrada del usuario para decidir si continúa la simulación de vuelo. |



### 📋 Caso 3: Sustentación en Despegue  

| Variable     | Tipo de Dato (Entrada/Salida/Constante) | Comentario |
|--------------|-----------------------------------------|------------|
| **peso**     | Float – Entrada       | El peso del avión. La sustentación debe ser mayor que este valor para que el avión pueda despegar. |
| **rho**      | Float – Constante     | La densidad del aire, un factor clave en la fórmula de sustentación. |
| **Cl**       | Float – Constante     | El coeficiente de sustentación. Depende de la forma del ala y el ángulo de ataque. |
| **A**        | Float – Constante     | El área alar (superficie del ala) del avión. |
| **v**        | Float – Entrada       | La velocidad del avión, que aumenta con el tiempo a medida que acelera en la pista. |
| **aceleracion** | Float – Constante  | La aceleración del avión en la pista. Se usa para incrementar la velocidad en cada paso de la simulación. |
| **L**        | Float – Salida        | La fuerza de sustentación calculada con la fórmula:  \(L = \tfrac{1}{2}\rho v^2 Cl A\). |
| **opcion**   | String – Entrada      | La entrada del usuario para seleccionar la opción del menú principal. |
