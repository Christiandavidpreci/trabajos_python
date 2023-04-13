print("FUNDAMENTOS DE PROGRAMACION DE PYTHON")
print("Christian Preciado")
#Crear una tupla de números enteros y calcular su suma y promedio.

tupla = (5,10,8,89,74,85,85,96,32,65,24,23,21,74,1,3,2,4,5,6,7,8,9)
print("La suma de la tupla: ",sum(tupla))
print("El promedio de la tupla: ",sum(tupla)/len(tupla))

#Crear dos tuplas de la misma longitud y crear una nueva tupla que contenga la suma de los elementos correspondientes de ambas tuplas.

suma = 0
t1 = (0,1,2,3,4,5,6,7,8,9)
t2 = (9,8,7,6,5,4,3,2,1,0)
for i in range(len(t1)):
        suma += (t1[i]+t2[i])

print("El resultado de la suma es: ",suma)

#Crear una tupla de nombres y ordenarla alfabéticamente.

nombres = ("Christian","Adriana","Daniela","Paula","Erika")
print(sorted(nombres))

#Crear una tupla de números y encontrar el valor mínimo y máximo.

print("El valor minimo de la tupla es: ", min(tupla))
print("El valor maximo de la tupla es: ", max(tupla))

#Crear una tupla de números y convertirla en una lista.

tupla = (5,10,8,89,74,85,85,96,32,65,24,23,21,74,1,3,2,4,5,6,7,8,9)
lista = list(tupla)
print(type(lista))

#Crear una tupla con los días de la semana y mostrar el tercer elemento.

semana = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
print(semana[3])

#Crear una tupla con números enteros y mostrar aquellos que son pares.

tupla = (5,10,8,89,74,85,85,96,32,65,24,23,21,74,1,3,2,4,5,6,7,8,9)
pares = 0 

for i in tupla:
    if i % 2 == 0:
          print("Los numeros pares son:",i)

#Crear una tupla con los meses del año y mostrar aquellos que tienen más de cinco letras.

meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
for mes in meses:
      if len(mes) > 5:
            print(mes)

#Crear una tupla con las edades de varias personas y mostrar la cantidad de personas mayores de 18 años.

edades = (22, 25, 62, 16, 50, 18, 19, 22, 24, 30)
contador = 0
for edad in edades:
    if edad > 18:
        contador += 1

print("Cantidad de personas mayores de 18 años:", contador)

#Crear una tupla de tuplas que contienen información de libros y mostrar el título del tercer libro.

libros = (
    ("El hobbit", "J.R.R. Tolkien", 1937),
    ("El código Da Vinci","Dan Brown",2003),
    ("Guerra y paz", " León Tolstói", 1867),
    ("Diario de Ana Frank", "Ana Frank", 1947),
    ("Lo que el viento se llevó", "Margaret Mitchell", 1936)
)

print(libros[2][0])