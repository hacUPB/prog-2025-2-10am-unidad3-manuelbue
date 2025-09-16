# Serie de Fibonacci básica

n = int(input("¿Cuántos números de la serie de Fibonacci deseas ver?: "))

a = 0
b = 1

print("Serie de Fibonacci:")

for i in range(n):
    print(a)       # mostramos el número actual
    siguiente = a + b  # calculamos el siguiente
    a = b              # movemos el valor de b a a
    b = siguiente 