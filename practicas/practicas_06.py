"""
Calculadora de descuentos: Escribe un programa que solicite al usuario un precio y un porcentaje de descuento, y calcule el precio final.
"""

precio = float(input("Dame el precio care monda: "))
porcentage = float(input("dame el porcentaje: "))

resultado =  precio - ((precio * porcentage) / 100)

print("Aqui esta tu care verga precio con el decuento: ",int (resultado))