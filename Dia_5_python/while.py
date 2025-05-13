import random
import time

# numAzar=random.randint(1,30)
# print(numAzar)

# dado=random.randint(1,6)
# print(dado)

## Adivinar el numero
# 
# n1=random.randint(1,50)
# n2=-1
# while n2!=n1:
  #      print(n1)
    # n2=int(input('Ingrese un numero '))
    # if n2<n1:
        # print('El numero a adivinar es mayor')
    # else:
        # print('El numero a adivinar es menor')
# print(f'Felicidades, acerto el numero que era {n1}')6

# # Ruleta rusa

# barril=random.randint(1,6)
# rul=int(input('Dispare : '))
# while rul!=barril:
#     rul=int(input('Dispare '))
# print('BANG!!!')

# La Florida 20%, La pintana 30%, Puente Alto 25%, San Joaquin 15%
# Grupo familiar: 1=>2%, 2 a 4 =>3%, 5 o mas=>4%
# Preguntar al usuario en que comuna vive
# Preguntar al usuario con cuantas personas vive
# EL arancel actual es de 200.000 por semestre
# Basados en las respuestas del usuario y en la informacion dada, calcular su descuento
'''
ej:
Ingrese su comuna: La Florida
Ingrese su grupo familiar (numero entero usted incluido): 4
El total del descuento es 23%
El total a pagar es $154.000
'''
# aran=200000
# flor=20
# pint=30
# alto=25
# san=15
# grup=0
# com=int(input('''En que comuna vive?
#               1.- La Florida
#               2.- La Pintana
#               3.- Puente Alto
#               4.- San Joaquin
#               '''))
# if com==1:
#     desc=flor
# elif com==2:
#     desc=pint
# elif com==3:
#     desc=alto
# else:
#     desc=san
# pers=int(input('Con cuantas personas vive incluyendolo a usted?'))
# if pers<=1:
#     grup+=1
# elif pers>=2 and pers<=4:
#     grup+=3
# else:
#     grup+=4
# total=grup+desc
# print(f'Su descuento actual es {total}%')
# t1=(aran*total)
# t2=(t1/100)
# t3=(aran-t2)
# print(f'Su total con el descuento aplicado es {t3}')

# Ludo

# peso=int(input('Ingrese su peso'))
# if 70<=peso:
#     print('Watona morbida')
# else:
#     print('Washita rica')

def carta():
    carta=random.choice([1,2,3,4,5,6,7,8,9,10,10,10,10])
    return carta
dealer=0
j1=0
print(f'Primera carta por para el dealer {carta}')
dealer+=carta
time.sleep(1)
carta()
dealer+=carta
print(f'Segunda carta por para el dealer {carta}')
time.sleep(1)
print(f'El dealer tiene actualmente {dealer}')
time.sleep(1)
carta()
j1+=carta
print(f'Primera carta para el jugador {carta}')
time.sleep(1)
carta()
j1+=carta
print(f'Segunda carta para el jugador {carta}')
time.sleep(1)
print(f'El jugador tiene actualmente {j1}')
time.sleep(1)
robo=int(input('''Usted quiere una carta mas?
               1.- Deme una carta mas
               2.- No quiero mas
               '''))
if j1==21:
    print('El jugador gano con Black Jack')
elif dealer<21:
    while 2!=robo and j1<=21:
        carta()        
        print(f'La carta que le salio es {carta}')
        j1+=carta
        if j1>=21:
            break
        print(f'El jugador tiene actualmente {j1}')
        robo=int(input('''Usted quiere una carta mas?
                   1.- Deme una carta mas
                   2.- No quiero mas
                   '''))
    print(f'El jugador tiene actualmente {j1}')
    if j1>=22:
        print('El jugador se paso y gana la casa')
    elif j1==dealer:
        print('Es un empate, nadie gana')
    elif dealer>=22:
        print('Perdio el dealer por haberse pasado de 21')
    elif dealer==21:
        print('Gano el dealer por haber sacado Black Jack')
    elif j1<=21:
        while dealer<17:
            carta()
            print(f'La siguiente carta para el dealer es {carta}')
            dealer+=carta
            print(f'El dealer tiene actualmente {dealer}')
            if dealer==21:
                print('El dealer tiene Black Jack por ende gana la casa')
            elif dealer>=22:
                print('Perdio el dealer por haberse pasado de 21')
            elif j1==dealer:
                print('Es un empate, nadie gana')
            elif j1<dealer:
                print('Gana la casa')
if j1>dealer and j1<22:
    print(f'Gano el jugador con {j1}')