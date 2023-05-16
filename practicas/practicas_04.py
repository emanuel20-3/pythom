"""
Ordenamiento de una lista: Pide al usuario que ingrese una lista de números y la ordena de forma ascendente.

lista_numeros = input("Ingreso una lista de numeros: ")
#lista_numeros = list(lista_numeros)
lista_numeros_2 = lista_numeros.split(",")
lista_numeros_2.sort()#te ordena las listas

print(lista_numeros_2)

"""

"""
Cálculo del índice de masa corporal (IMC): Pide al usuario que ingrese su peso y altura y calcula su IMC.
"""
peso = float(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura: "))

imc = peso / (altura*altura)
imc_2 = round(imc, 2)

if imc_2 >= 40:
    print("Estas como un boloncho, se te va a parar el mango")

elif imc_2 <= 15:
    print("Come yuca con suero care verga")

else:
    print("Estas lite")





