# ejercicio 1
# quintil=0
# empleo=0
# sub=0
# bon1=60000
# bon2=40000
# edad=0
# quintil=int(input('¿A que Quintil pertenece? (1-5) '))
# print('--------------------------------------------')
# empleo=int(input('''¿Usted esta trabajando?
# 1.- Si
# 2.- No
# '''))
# if quintil<=2 and empleo==2:
# sub+=350000
# sub+=bon1
# elif quintil<=2 and empleo==1:
# sub+=280000
# sub+=bon1
# elif quintil==3 and empleo==2:
# sub+=250000
# elif quintil==3 and empleo==1:
# sub+=200000
# print('--------------------------------------------')
# edad=int(input('Ingrese su edad porfavor '))
# if quintil<=3 and edad>=65:
# sub+=bon2
# print('--------------------------------------------')
# print(f'El valor del subsidio de arriendo es: {sub}')
# ejercicio 2
import random
n1=0
n2=0
n3=0
n5=-1
n6=-1
intentos=3
n1=int(input('Ingrese limite inferior: '))
print('--------------------------------------------')
n2=int(input('Ingrese limite superior: '))
if n1>=n2:
    print('Limite superior es inferir al otro limite, porfavor ingrese bien los limites')
    print('--------------------------------------------')
elif n1<n2:
    n3=random.randint(n1,n2)
    print(n3)
    n4=int(input('Intente adivinar el numero: '))
    print('--------------------------------------------')
    while n4!=n3 or n5!=n3 or n6!=n3:
        intentos-=1
        if intentos==0:
            break
        elif n4!=n3 and intentos==1:
            print('El numero es mayor')
            print('Te dare una pista: ')
            if n5>=n4 and n5!=n3:
                print(f'El numero que buscas esta mas cerca de {n5} que de {n4}')
                n6=int(input('Intente la ultima: '))
                print('--------------------------------------------')
            elif n5<=n4 and n5!=n3:
                print(f'El numero que buscas esta mas cerca de {n4} que de {n5}')
                n6=int(input('Intente la ultima: '))
                print('--------------------------------------------')
        elif n4<n3:
            print('El numero es mayor')
            n5=int(input('Intente de nuevo: '))
            print('--------------------------------------------')
        elif n4>n3:
            print('El numero es menor')
            n5=int(input('Intente de nuevo: '))
            print('--------------------------------------------')
if n4==n3:
    print('Felicitaciones, pudiste adivinar')
elif n5==n3:
    print('Felicitaciones, pudiste adivinar')
elif n6==n3:
    print('Felicitaciones, pudiste adivinar')
else:
    print(f'Perdiste, el numero correcto era {n3}')
# Me dolio mucho la cabeza solo tener que organizar esto