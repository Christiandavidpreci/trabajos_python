print("CURSO FUNDAMENTOS DE PYTHON")
print("Christian Preciado\n")
dato=int(input('Digite el número a verfificar si es múltiplo de 3: '))
if(dato%3==0):
    print('El número {} es múltiplo de 3'.format(dato))
else:
    print(f'El número: {dato} no es multiplo de 3')