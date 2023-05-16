"""
Calculadora de descuentos: Escribe un programa que solicite al usuario un precio y un porcentaje de descuento, y calcule el precio final.
"""
"""
precio = float(input("Dame el precio care monda: "))
porcentage = float(input("dame el porcentaje: "))

resultado =  precio - ((precio * porcentage) / 100)

print("Aqui esta tu care verga precio con el decuento: ",int (resultado))
"""

"""
Validación de correos electrónicos: Escribe un programa que solicite al usuario una dirección de correo electrónico y valide si cumple con ciertos requisitos, como la inclusión de un signo "@" y un dominio válido.
"""

def validar():
    correo = input("Ingresa tu corre: ")
    if correo.find("@")==-1 and correo.find("gmail")==-1 and correo.find("hotmail")==-1:
        print("El correo electrónico ingresado no es válido")
        validar()
    else:
        print("El correo electrónico ingresado es válido")
        
validar()