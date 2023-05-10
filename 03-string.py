#strings

mi_string= "mi string"

print(len(mi_string))

mi_nuevo_string_linea= "este es mi string\ncon salto de linea"
print(mi_nuevo_string_linea)

mi_tab_string= "\tmi string con tabulacion"
print(mi_tab_string)

mi_escape_string= "\teste es un string \n escapado"
print(mi_escape_string)

#fomateo

nombre, apellido, edad= "emanuel", "espitia", 19

print("mi nombre es {} {} y mi edad es {}" .format(nombre, apellido, edad))
print("mi nombre es %s %s y mi edad es %d" %(nombre, apellido, edad))
print(f"mi nombre es {nombre} {apellido} y mi edad es {edad}")

# desenpaquetado de caracteres
lengua= "python"
a, b, c, d, e, f= lengua 
print(a)
print(b)

#divicion

lenguage_slice= lengua[1:3]
print(lenguage_slice)

lenguage_slice= lengua[1:]
print(lenguage_slice)

lenguage_slice= lengua[-2]
print(lenguage_slice)

lenguage_slice= lengua[0:6:2] 
print(lenguage_slice)


#reversa
reversa_lenguage= lengua[::-1]
print(reversa_lenguage)

#funciones
print(lengua.capitalize())
print(lengua.upper())
print(lengua.count("p"))
print(lengua.isnumeric())
print("2".isnumeric())
print(lengua.lower())
print(lengua.upper().isupper())
print(lengua.startswith("py"))





