""" 
grado = input("temperatura (en enteros): ")
grado = int(grado)
resultado = (grado* 9/5) + 32 

print("Aqui esta tu monda:",resultado, "F°")
"""
"""
while True:
    try:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        break
    except ValueError:
        print("Por favor, ingrese un valor numérico para la base y la altura.")

area = (base * altura) / 2

print("El área del triángulo es:", area)
"""

while True:
    try:
        n_1= float(input("numero uno: "))
        n_2= float(input("numero dos: "))
        break
    except ValueError:
        print("care verga")

    resultado = n_1 + n_2

    print(int(resultado))


