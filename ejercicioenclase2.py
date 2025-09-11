numero = int(input("ingrese el numero entero: "))
while numero < 0:
    numero = int(input("ingrese nuevamente un numero positivo: "))
acum = 0
for cont in range(1, numero+1):
    if cont % 2 == 0:
        acum += cont
print(F"la suma de los pares es: {acum}")

mensaje = "universidad pontificia Bolivariana"
numero = int(input("ingrese el numero entero positivo: "))
for i in range(numero):
    print(f"{i+1}. {mensaje}")
    
