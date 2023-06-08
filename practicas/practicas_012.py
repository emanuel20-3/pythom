import math

"""
Implementar una función que determine si una cadena de texto es un palíndromo.
"""

# def pali(palabra):
#     inverso = palabra[::-1]
#     if palabra == inverso:
#         return "Es palindromo"
#     else:
#         return "No es palindromo"
# print(pali("coco"))

"""
Implementar un programa que calcule el área y perímetro de un círculo a partir de su radio.
"""
# radio = float(input("Dame el radio care verga: "))
# area = 3.15 * math.pow(radio, 2)
# perimetro = 2 * 3.14 * radio

# print(f"Aqui esta tu area {area: 2f} y tu permetro {perimetro: 2f} de tu circulo")

"""
Crear una función que reciba una lista de palabras y devuelva la palabra más larga.
"""

def palabras(grande):
    n= len(grande)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(grande[j]) > len(grande[j+1]):
                grande[j], grande[j+1] = grande[j+1], grande[j] 
    print(grande[-1])
palabras(["emanuel", "espita", "anaya", "vergalaraga"]) 