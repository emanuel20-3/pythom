#variables 
#nombrar las variables con solo minusculas el cual es una buena practica
mi_string_variable= "mi string variable"
print(mi_string_variable)

mi_int_variable= 20
print(mi_int_variable)

mi__float_variable= 2.3
print(mi__float_variable)

mi__complex_variable= (3+2j)
print(mi__complex_variable)

mi__bool_variable= True
print(mi__bool_variable)

#concatenacion de variables en print
print(mi_int_variable,mi_string_variable) #varibales en cadena de texto

#algunas funciones del sistema
print(len(mi_string_variable))

#variables en una sola linea-no abusar de esto
nombre,apellido,alias,edad= "emanuel", "espitia", "ema", 19
print("mi nombre es:",nombre, apellido, ".mi alias es:",alias, ".mi edad es:", edad)

mi_nombre= input("cual es tu nombre: ")
mi_apellido= input("cual es tu apellido: ")

#inputs
print(mi_nombre)
print(mi_apellido)
