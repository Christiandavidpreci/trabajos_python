print("FUNDAMENTOS DE PROGRAMACION DE PYTHON")
print("Christian Preciado")
#Crear un diccionario vacío:

diccionario = {}

#Agregar elementos a un diccionario:

diccionario ["Clave 1"] = 101
diccionario ["Clave 2"] = 202
diccionario ["Clave 3"] = 303
diccionario ["Clave 4"] = 404
diccionario ["Clave 5"] = 505

print(diccionario )

#Acceder a un valor en un diccionario:

print(diccionario ["Clave 4"])

#Verificar si una llave existe en un diccionario:

print(diccionario .keys())

#Eliminar un elemento de un diccionario:

print(diccionario .pop("Clave 1"))

#Imprimir las llaves de un diccionario:

print(diccionario .keys())

#Imprimir los valores de un diccionario:

print(diccionario .values())

#Imprimir las llaves y valores de un diccionario:

print(diccionario .items())