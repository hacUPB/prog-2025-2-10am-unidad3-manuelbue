# Algoritmo de la serie de Fibonacci

# Pedir al usuario cuántos números quiere mostrar
n = int(input("¿Cuántos números de la serie de Fibonacci deseas ver?: "))

# Definir los dos primeros números de la serie
a, b = 0, 1

print("\nSerie de Fibonacci:")

# Generar la serie
for i in range(n):
    print(a, end=" ")  # mostrar el número
    a, b = b, a + b    # actualizar los valores
