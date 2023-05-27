# Escribe una función llamada buscar_duplicados(lista) que tome una lista como parámetro y devuelva una nueva lista con los elementos duplicados encontrados en la lista original.

# def duplicado(lista):
#     copia = []
#     for i in lista:
        

# duplicado([1,1,6,6,2,3,8,4,0])

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Últimos i elementos ya están en su lugar correcto
        for j in range(0, n-i-1):
            # Recorrer el arreglo de 0 a n-i-1
            # Intercambiar elementos si el elemento encontrado es mayor que el siguiente
            if arr[j] > arr[j+1]:
                print(arr[j+1])
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lista)
print("Lista ordenada:")
print(lista)
