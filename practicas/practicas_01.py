"""
ejersicio #1: caluladora

tu tarea cabeza de monda es hacer una calculadora con las siguientes caracteristicas. 

- preguntar al usuario con el metodo input() que ingrese el numero

- preguntar por medio de un input, cual es la operacion aritmetica que desea

- preguuntar el segundo valor de la operacion

- ya sea por medio de condicionales o lo que se te ocurra, has la logica para que dependiente de la operacion el resultado corresponda

- muestra ek resultado en consola


nota : tener en cuanta que todo valor que devuelve un input es un string
"""

# pon tu popo de cogigo aca

"""
n_1= input("Ingresa un numero care monda: ")

operacion = input("Que operacion quieres hacer (+, -, *, %): ")

n_2 = input("Dame el segundo numero care verga: ")

n_1 = float(n_1)
n_2 = float(n_2)

if operacion == "+" :
    resultado= n_1 + n_2

elif operacion == "-":
    resultado= n_1 - n_2

elif operacion == "*":
    resultado= n_1 * n_2

elif operacion == "/":
    resultado= n_1 / n_2

else : 
    print("No se puede care monda")

print("Aqui esta tu care verga resultado: ", int(resultado))
"""

"""
ejersicio #2: cambio de divisas 

care verga este ejersicio es la misma monda del de arriba solo con algunas trampillas, la tarea es convertir un valor ingresado en pesos a dolares, euros y libras 

cambios: 

dolar = pesos * 0.00022
euro = pesos * 0.00019
libra = pesos * 0.00016

- preguntar por medio en un input cual es su valor es pesos

- pregunta cual es la moneda de cambio

- hacer ka logica para que dependiendo de la moneda de cambio realizar la operacion correspondiente

"""
peso = input("Dame tu valor en pesos: ")

moneda_de_cambio = input("moneda de cambio (dolar, euro, libra): ")

moneda_de_cambio = moneda_de_cambio.lower()

peso = float(peso)

if moneda_de_cambio == "dolar":
    resultado = peso * 0.00022

elif moneda_de_cambio == "euro":
    resultado = peso * 0.00019

elif moneda_de_cambio == "libra":
    resultado = peso * 0.00016

else :
    print("No se puede care monda")

print(f"Aqui esta tu valor {peso} a {moneda_de_cambio}: ")


