# Crear un menu de carrito con las siguientes opciones
# 1.- Ingresar nombre el usuario
# sera mostrado en la boleta, con un saludo
# 2.- Comprar, poner productos para poder comprar con su precio correspondiente
# 3.- Sacar boleta, calcular el precio neto y el precio mas IVA. Mostrando totales
# Bonus contar la cantidad de articulos
# 4.- Salir
# Consideraciones: 
# Por lo menos 3 productos
# No hay limite de compra
# Se puede salir en cualquier momento

# papa=0
# cebolla=0
# tomate=0
# user='Cliente'

while True:
    try:
        op=int(input('''Que es lo que desea hacer
                    1.- Ingresar usuario
                    2.- Comprar
                    3.- Ver boleta
                    4.- Salir
                    '''))
        match op:
                case 1:
                    user=input('Bienvendio a X-Mart, ingrese su nombre porfavor')
                case 2:
                        productos=int(input('''A continuacion la lista de productos disponibles
                            1.- Papa 1kg x 750
                            2.- Cebolla 1kg x 500
                            3.- Tomate 1kg x 1300
                            4.- Salir
                            '''))
                        match productos:
                            case 1:
                                cant1=int(input('Cuanto va a llevar?'))
                                papa+=cant1
                            case 2:
                                cant2=int(input('Cuanto va a llevar?'))
                                cebolla+=cant2
                            case 3:
                                cant3=int(input('Cuanto va a llevar?'))
                                tomate+=cant3
                            case 4:
                                print()
                case 3:
                    papa*=750
                    cebolla*=500
                    tomate*=1300
                    total=papa+cebolla+tomate
                    iva=total*1.19
                    print(f'Saludos {user} aqui tiene su boleta')
                    if papa>0 and cebolla>0 and tomate>0:
                        print(f'''
                            Papa = {papa}
                            Cebolla = {cebolla}
                            Tomate = {tomate}
                            Total = {total}
                            +IVA = {iva}
                            ''')
                    elif papa==0 and cebolla>0 and tomate>0:
                        print(f'''
                            Cebolla = {cebolla}
                            Tomate = {tomate}
                            Total = {total}
                            +IVA = {iva}
                            ''')
                    elif papa>0 and cebolla==0 and tomate>0:
                        print(f'''
                            Papa = {papa}
                            Tomate = {tomate}
                            Total = {total}
                            +IVA = {iva}
                            ''')
                    elif papa>0 and cebolla>0 and tomate==0:
                        print(f'''
                            Papa = {papa}
                            Cebolla = {cebolla}
                            Total = {total}
                            +IVA = {iva}
                            ''')
                    elif papa==0 and cebolla==0 and tomate>0:
                        print(f'''
                            Tomate = {tomate}
                            Total = {total}
                            +IVA = {iva}
                            ''')
                    elif papa>0 and cebolla==0 and tomate==0:
                        print(f'''
                            Papa = {papa}
                            Total = {total}
                            +IVA = {iva}
                            ''')
                    elif papa==0 and cebolla>0 and tomate==0:
                        print(f'''
                            Cebolla = {cebolla}
                            Total = {total}
                            +IVA = {iva}
                            ''')
                case 4:
                    break
    except Exception:
        print('Datos mal ingresados, porfavor intente de nuevo')
print('Gracias por venir a X-Mart')

#### Promedios por cantidad de alumnos ####
# Pedir cantidad de alumnos
# pedir notas por cada alumno
# promediar a cada alumno 
# y mostrar si aprueba o reprueba
# Bonus, mostrar promedio de todos los alumnos
# ingresados

'''Ingrese cant de alumnos: 5
Ingrese cantidad de notas del alumno 1 :3
Ingrese la nota 1 del alumno 1
Ingrese la nota 2 del alumno 1
Ingrese la nota 3 del alumno 1
El promedio del alumno 1 es : 5.6
El alumno 1 Aprobo
'''

