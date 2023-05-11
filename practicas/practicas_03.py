"""
2. Crear un programa que pida al usuario ingresar un número entero y luego imprima todos los números pares desde 0 hasta ese número.
"""
"""
n_1 = int(input("Ingresa un numero entero care monda: "))

#for i in range(0, n_1 + 1, 2):
    #print(i)

for i in range(n_1 + 1):
    if i % 2 == 0:
        print(i)
"""

"""
3. Crear un programa que pida al usuario ingresar una cadena de caracteres y luego imprima su longitud.
"""

monda = str(input("Ingresa cualquier monda: "))
monda_sin_espacios = monda.replace(" ", "")


print(len(monda_sin_espacios))