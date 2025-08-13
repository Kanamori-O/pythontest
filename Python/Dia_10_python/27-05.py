# menu tarjeta de credito
deuda=100000
op2=0

while True:
    while True:
        try:
            print(f'Su deuda en su tarjeta es actualmente de {deuda}')
            op=int(input('''
                         Selecciona una opcion
                         1.- Pagar deuda de la tarjeta 
                         2.- Comprar
                         3.- Salir
                         '''))
            break
        except Exception:
            print('Ingrese una opcion valida porfavor')
    match op:
        case 1:
            while True:
                try:
                    pago=int(input('Ingrese un monto '))                   
                    if pago>deuda:
                        print('El monto que ingreso excede su deuda')
                    elif pago>0:
                        deuda-=pago
                        print(f'Su deuda actual es {deuda}')
                    else:
                        print('El monto que ingreso no es valido')
                    break
                except Exception:
                    print('Ingrese un monto valido')
        case 2:
            while True:
                try:
                    op2=int(input('''Que desea hacer?
                                     1.- Comprar
                                     2.- Salir
                                     '''))
                    match op2:
                        case 1:
                            compra=int(input('Ingrese el monto a pagar '))
                            deuda+=compra
                        case 2:
                            print('Saliendo...')
                            break
                        case _:
                            print('La opcion es invalida')
                    break
                except Exception:
                    print('Ingrese caracter valido')
        case 3:
            print('Saliendo...')
            break
        case _:
            print('Opcion invalida')
            