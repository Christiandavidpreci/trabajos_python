print("Curso: Introducioon a la Big Data")
print("Nombre:Christian Preciado")
letra= input("Ingrese una letra:")

if len(letra)!= 1:
    print("No se peuede procesar el dato.Deve ingresar una sola letra")
elif letra in "aeiouAEIOU":
    print("Es vocal")
else:
    print("No es vocal")  