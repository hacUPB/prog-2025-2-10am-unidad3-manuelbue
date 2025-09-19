'''
import modfunciones

numero = int(input("ingrese un numero mayor que 1: "))
modfunciones.primo(numero)
variable = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
modfunciones.fibonacci(variable)
multiplicando = int(input("Ingrese el número entero: "))
modfunciones.tabla(multiplicando)
'''

from modfunciones import *
def main():
    while True:
        opc = menu()
        match opc:
            case 1:
                print("Calcula si un numero es primo.")
                valor = int(input("Ingrese un numero entero mayor que 1: "))
                primo(valor)
            case 2: 
                print("Imprime la serie de Fibonacci")
                num =  int(input("Ingrese el número de términos de la serie de Fibonacci: "))
                fibonacci(num)
            case 3:
                print("Imprime la tabla de multiplicar")
                num= int(input("Ingrese el número entero: "))
                tabla(num)
            case 4:
                break
            case _:
                print("la opcion que ingreso no es valida")


if __name__ == "__main__":
    main()