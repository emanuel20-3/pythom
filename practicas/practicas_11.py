"""
Crea una función que tome una lista de palabras y devuelva la lista ordenada según la longitud de las palabras.
"""

# def orden_palabras(orden):
#     n= len(orden)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if len(orden[j]) > len(orden[j+1]):
#                 orden[j], orden[j+1] = orden[j+1], orden[j] 
#     print(orden)
# orden_palabras(["emanuel","coste","puta","y","perra"])

"""
Escribe una función que tome una lista de números y devuelva la mediana de la lista.
"""
# def numeros(media):
#     suma = 0
#     for i in media:
#         suma = suma + i
#     print(suma / len(media))
# numeros([1,2,3,4,5,6,7,8])

"""
Crea una función que tome una lista de palabras y devuelva la palabra más larga de la lista.
"""

def larga(palabra):
    n= len(palabra)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(palabra[j]) > len(palabra[j+1]):
                palabra[j], palabra[j+1] = palabra[j+1], palabra[j] 
    print(palabra[-1])

larga(["emanuel","espita","anaya","si la vida"])