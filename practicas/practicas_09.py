"""
Escribe una función llamada factorial(n) que calcule el factorial de un número entero n. El factorial de un número se define como el producto de todos los enteros positivos desde 1 hasta ese número.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
         return n * factorial(n - 1)
    
print(factorial(5))


