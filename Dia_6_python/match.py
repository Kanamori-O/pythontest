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
    try:
        n1=int(input('Ingrese un numero'))
        n2=int(input('Ingrese un numero'))
        print(f'El resultado de la division es {n1/n2}')
    except ZeroDivisionError as nombre_de_excepcion:
        # Código para manejar la excepción
        print(f"Se produjo una excepción: {nombre_de_excepcion}")


def calcu():
    while True:
        try:
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
                        division()
                
                case 5:
                    print('Saliendo...')
                    break
                case _:
                    print('Opcion invalida')
        except Exception:
            print('Solo puede ingresar numeros, no caracteres')

# calcu()


try:
    op=int(input('Ingrese un numero'))
except Exception:
    print('Solo puede ingresar numeros, no caracteres')