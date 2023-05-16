"""
cadena = str(input("Escrebe cual quier monda care loco: "))
monda_mayuscula = cadena.upper()

print(monda_mayuscula)
"""

"""
Escriba un programa que tome una lista de números enteros y devuelva una lista que contenga solo los números impares de la lista original.
"""

monda = [1,2,3,4,5,6,7,8,9]
monda_2 = []

for i in monda:
    if i % 2 == 1:
        monda_2.append(i)
        print(i)


