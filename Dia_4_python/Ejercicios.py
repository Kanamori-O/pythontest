### Ejercicios varios
# Nivel 2

#1 Pida al usuario un numero y clasifiquelo como par o impar, muestre los pares e impares de el uno hasta ese numero

#2 Pida al usuario ingresar numeros, al fianl debe mostrar cuantos numeros se ingresaron y mostrar la suma de todos ellos, para terminar, debe poner la palabra salir

#3 Pida al usuario ingresar un numero y multiplialo por un numero al azar entre 2 y 8. Si el numero es mayor que 50, logro la meta, si no, intente nuevamente

#4 Ingresar un numero positivo, multiplicarlo por 5, restarle 8, sumarle 3 y dividirlo por 2

# Ejercicio 1
"""
num=int(input('Ingrese un numero: '))
if num%2==0:
    print('Es par')
else:
    print('Es impar')

print(f'los numeros pares entre 1 y {num} son: ')

for i in range(1,num+1):
    if i%2==0:
        print(i)

print(f'los numeros impares entre 1 y {num} son: ')

for i in range(1,num+1):
    if i%2!=0:
        print(i)
"""
# Ejercicio 2
'''
cont=0
total=0
opc=""
while (opc!=2):
    print('1) Ingresar nuevo numero')
    print('2) Salir')
    opc=int(input())
    if opc==1:
        a=int(input('Ingrese el numero que desea: '))
        cont+=1
        total+=a
print(f'La cantidad de numeros ingresados son : {cont}')
print(f'La suma es : {total}')
'''
# Ejercicio 3
'''
from random import randint
a=0
b=randint(2,8)
while(a*b<50):
    a=int(input('Ingrese el valor de a: '))
    b=randint(2,8)
    print(b)
    print(f'la multiplicacion es {a}x{b} = {a*b}')
print('Logro la meta!')
'''
# Ejercicio 4
'''
num=-1
while num<0:
    num=int(input('Ingrese un numero: '))
    if num<0:
        print('Ingreso un valor negativo! vuelva a intentar')
total=num*5
total=total-8
total=total+3
total=total/2
print('el valor final es {total}')
'''
