#tuplas 

mi_tupla = tuple()
mi_otra_tupla = ()

mi_tupla = (19, 1.83, "emanuel", "espitia")
mi_otra_tupla = (12, 13, 15)

print(mi_tupla)
print(type(mi_tupla))

print(mi_tupla[1])
print(mi_tupla[-1])
#print(mi_tupla[4]) indexerror
#print(mi_tupla[-5]) indexerror

print(mi_tupla.count(19)) #te dice cuantos elementos hay en la tupla
print(mi_tupla.index(1.83)) #te dice donde esta el valor en la tupla

#mi_tupla[1] = 1.90 'tuple' object does not support item assignment

mi_suma_tuplas = mi_otra_tupla + mi_tupla
print(mi_suma_tuplas)

print(mi_suma_tuplas[3:6]) 

""" 
NameError: name 'mi_tupla' is not defined:
del mi_tupla
print(mi_tupla)
"""


