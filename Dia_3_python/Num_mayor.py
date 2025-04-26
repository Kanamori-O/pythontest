# # Ingrese 3 numeros y que muestre que numero es mayor
# print('Ingrese 3 numeros')
# n1=int(input())
# n2=int(input())
# n3=int(input())

# m=max(n1,n2,n3)
# n=min(n1,n2,n3)

# print('El numero mayor es', m)
# print('El numero menor es', n)

import time

palabra=input('Ingrese una frase ')
cont=0
vocales=0
cons=0
for i in palabra.lower():
    cont+=1
    print(cont, i)
    if i in 'aeoiu':
        vocales+=1
    else:
        cons+=1
print('La cantidad de caracteres son', cont)
print('La cantidad de vocales son', vocales)