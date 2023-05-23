"""
Conversor de bases numéricas: Crea un programa que convierta un número en decimal a binario, octal o hexadecimal según la elección del usuario.
"""

n = int(input("Dijita tu puto numero: "))
convercions = input("Converciones (binario, octal, hexadecimal): ")

resi = []
if convercions == "binario" :
    while n > 0:
        resi.append(n % 2)
        n = n // 2
    cadena = ''.join(map(str, resi))
    cadena_monda = cadena[::-1]
    print(cadena_monda)

elif convercions == "octal" :
    while n > 0:
            resi.append(n % 8)
            n = n // 8
    cadena = ''.join(map(str, resi))
    cadena_monda = cadena[::-1]
    print(cadena_monda)

elif convercions == "hexadecimal":
    while n > 0:
            resi.append(n % 16)
            n = n // 8
    cadena = ''.join(map(str, resi))
    cadena_monda = cadena[::-1]
    print(cadena_monda)

