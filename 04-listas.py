#listas

mi_lista = list()
mi_other_list = [] 

print(len(mi_lista))

mi_lista = [19, 18, 20, 24, 34]

#print(mi_lista)

mi_other_list = [19, 1.83, "emanuel", "espitia"]
print(mi_other_list[0])
print(mi_other_list[1])
print(mi_other_list[-1])
print(mi_other_list[-3])

edad, altura, nombre, apellido = mi_other_list
print(edad)

#print(mi_other_list + mi_lista) se pueden sumar lista (agruparlas)

mi_other_list.append("sura")#da un nuevo objeto a la lista en la ultima posicion
print(mi_other_list)

mi_other_list.insert(1, "negro")#da un nuevo objeto a la lista en la posicion que quieras 
print(mi_other_list)

mi_other_list.remove("negro")#quita algo de la lista
print(mi_other_list)

mi_lista.pop(0)#quita un elemento de la lista (por defecto el ultimo)
print(mi_lista)

"""
mi_pop_elemento= mi_lista.pop(3)
print(mi_pop_elemento)
"""

del mi_lista[0]
print(mi_lista)

mi_nueva_kista = mi_lista.copy()

mi_lista.clear()
print(mi_lista)
print(mi_nueva_kista)

mi_nueva_kista.reverse()
print(mi_nueva_kista)


