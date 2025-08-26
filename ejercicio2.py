# determinar si un numero es par o impar
numero = int(input("ingrese un numero entero: "))
residuo = numero % 2
#si residuo es 0 es par
if residuo == 0:
    print(numero, "es par")
else:
    print(numero, "es impar")    
    