#Crea una lista vacía llamada numeros e introduce los números del 1 al 5. Luego, muestra la lista por pantalla.
#Crea una lista con los nombres de tus amigos y muestra por pantalla el primer elemento de la lista.
#Crea una lista con los números del 1 al 10 y muestra por pantalla los números pares.
#Crea una lista con los nombres de tus amigos y muestra por pantalla el último elemento de la lista.
#Crea una lista con los números del 1 al 10 y muestra por pantalla el último elemento de la lista.
#Crea una lista con los números del 1 al 10 y muestra por pantalla los números impares.
#Crea una lista con los nombres de tus amigos y añade un nuevo amigo a la lista. Luego, muestra la lista por pantalla.
#Crea una lista con los números del 1 al 10 y muestra por pantalla el primer y el último elemento de la lista.
#Crea una lista con los nombres de tus amigos y muestra por pantalla el número de elementos de la lista.
#Crea una lista con los números del 1 al 10 y muestra por pantalla la suma de todos los elementos de la lista.
numeros = [1,2,3,4,5]
print(numeros)
nombres=["kevin","shakira","Bruce","Rene","Lenin"]
print(nombres[0])
pares=[1,2,3,4,5,6,7,8,9,10]
for e in pares:
    if e%2==0:
        print("El numero es par",e)

lista=[1,2,3,4,5,6,7,8,9,10]
suma=0
for e in lista:
    suma=suma + e
print(suma)


lista=[1,2,3,4,5,6,7,8,9,10]
suma=0
for e in lista:
    suma +=e

print(suma)
print(sum(lista))