"""
Encontrar el máximo y mínimo de una lista de números.


mi_max = input("Ingresa una lsita de numeros care monda: ")
mi_max = list(mi_max)
mi_maxint = map(int, mi_max)
mi_max.sort()

print(f"Aqui esta tu numero menor {mi_max[0]} y aqui esta tu numero mayor {mi_max[-1]}")

"""

"""
Verificar si una cadena es un palíndromo.
"""

pa = input("Ingresa una palabra bro: ")

if pa == pa[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")





