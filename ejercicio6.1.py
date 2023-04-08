nombre=input("ingrese nombre:")
print("Ingrese 1 si pertenece al departamento de atencion al cliente ")
print("ingrese 2 si pertenece al departamento de logistica")
print("ingrese 3 si pertenece al departamento de gerencia ")

departamento=int(input("digite al departamento que pertenece:"))
años=int(input("ingrese los años de servicio:"))
if departamento==1:
    if años==1:
        print("hola",nombre,"por tu",años,"año de trabajo, obtendras 6 dias de vacaciones")
    if años>=2 and años<=6:
        print("hola",nombre,"por tu",años,"año de trabajo, obtendras 12 dias de vacaciones")
    if años>7:
        print("hola",nombre,"por tu",años,"año de trabajo, obtendras 20 dias de vacaciones")
if departamento==2: 
    if años==1:
         print("hola",nombre,"por tu",años,"año de trabajo, obtendras 6 dias de vacaciones")                
    if años>=2 and años<=6:
         print("hola",nombre,"por tu",años,"año de trabajo, obtendras 14 dias de vacaciones")
    if años>7:
        print("hola",nombre,"por tu",años,"año de trabajo, obtendras 22 dias de vacaciones")
if departamento==3:      
    if años==1:
        print("hola",nombre,"por tu",años,"año de trabajo, obtendras 10 dias de vacaciones")
    if años>=2 and años<=6:
         print("hola",nombre,"por tu",años,"año de trabajo, obtendras 20 dias de vacaciones")
    if años>7:
        print("hola",nombre,"por tu",años,"año de trabajo, obtendras 30 dias de vacaciones")