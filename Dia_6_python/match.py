def suma():
    n1=int(input('Ingrese un numero'))
    n2=int(input('Ingrese un numero'))
    print(f'El resultado de la suma es {n1+n2}')
def resta():
    n1=int(input('Ingrese un numero'))
    n2=int(input('Ingrese un numero'))
    print(f'El resultado de la resta es {n1-n2}')
def multi():
    n1=int(input('Ingrese un numero'))
    n2=int(input('Ingrese un numero'))
    print(f'El resultado de la multiplicacion es {n1*n2}')
def division():
    n1=int(input('Ingrese un numero'))
    n2=int(input('Ingrese un numero'))
    print(f'El resultado de la division es {n1/n2}')


while True:
    op=int(input('''Ingrese una opcion
                 1.- Suma
                 2.- Resta
                 3.- Multiplicacion
                 4.- Division
                 5.- Salir
                 '''))
    match op:
        case 1:
            print('Procediendo a la suma')
            suma()
        case 2:
            print('Procediendo a la resta')
            resta()
        case 3:
            print('Procediendo a la multiplicacion')
            multi()
        case 4:
            print('Procediendo a la division')
            division
        case 5:
            print('Saliendo...')
            break
        case _:
            print('Opcion invalida')
