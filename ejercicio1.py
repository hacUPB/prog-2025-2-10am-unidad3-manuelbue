nombre = input("Ingresa tu nombre y apellido:")
#Opcion 2
print ("Bienvenido: ", nombre)
#Calcular el IMC de la persona
#Leer peso, altura
peso = input("Ingresa tu peso en kg: ")
peso= float(peso)
altura = input("Ingresa tu talla en metros: ")
altura= float(altura)
#Calculos
imc = peso/altura**2
#Mostrar IMC
print("Tu IMC = ", imc)
if imc < 18.5:
    print("Bajo peso")
if imc >= 18.5 and imc < 25:
    print("Peso normal")
if imc >= 25 and imc < 30:
    print("Sobrepeso")
if imc >= 30:
    print("Obesidad")
if imc >= 40:
    print("Obesidad morbida")
if imc >= 50:
    print("Obesidad extrema")



if imc < 18.5 :
    mensaje = "bajo peso"
elif imc < 25:
    mensaje = "peso normal"
elif imc < 35:
    mensaje = "obseidad tipo 1"
elif imc < 50: 
    mensaje = "obesidad tipo 2"
else:
    mensaje = "obsesidad extrema"

print(f"paciente {nombre}, tiene un IMC de {imc: 0.2f} y su condicion es {mensaje}.")

## ejercicio en clase
numero = int(input("ingrese un numero entero"))
print(numero % 3 )
if numero % 3 == 0:
    print("el numero {numero} es divisible en 3")
