## Operadores Aritmeticos
| Operador | Descripción                 | Ejemplo    | Resultado |
|----------|-----------------------------|------------|-----------|
| +      | Suma                        | 5 + 2    | 7       |
| -      | Resta                       | 5 - 2    | 3       |
| *      | Multiplicación              | 5 * 2    | 10      |
| /      | División (punto flotante)   | 5 / 2    | 2.5     |
| //     | División entera             | 5 // 2   | 2       |
| %      | Módulo (resto de división)  | 5 % 2    | 1       |
| **     | Exponente                   | 5 ** 2   | 25      |

## Tipos de datos numéricos en Phyton
| Tipo de Dato | Descripción                              | Ejemplo        |
|--------------|------------------------------------------|----------------|
| int        | Entero (número sin parte decimal)        | 10, -5     |
| float      | Punto flotante (decimal)                 | 3.14, -2.5 |
| complex    | Número complejo                          | 3+4j         |
| bool       | Booleano (True o False)                  | True, False|

## Combinaciones Válidas de Tipos en Operaciones
| Operación        | Tipos Involucrados     | Resultado | Comentario                                 |
|------------------|------------------------|-----------|--------------------------------------------|
| int + int      | int, int           | int     | Suma de enteros                            |
| int + float    | int, float         | float   | El entero se convierte a flotante          |
| float * float  | float, float       | float   | Multiplicación de decimales                |
| int / int      | int, int           | float   | Siempre da un flotante                     |
| int // float   | int, float         | float   | División entera, resultado con decimales   |
| int + complex  | int, complex       | complex | Resultado se convierte a complejo          |
| bool + int     | bool, int          | int     | True = 1, False = 0      