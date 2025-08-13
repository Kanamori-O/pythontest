# Nuevos diccionarios y manipulacion de datos


juegos={
    1:{
        'nombre': 'Metroid Dread',
        'precio': 50000,
        'code': 'MMdd23'
    },
    2:{
        'nombre': 'Pikmin 4',
        'precio': 55000,
        'code': 'pKMn2022'
    }
}

'''
el codigo debe tener 2 mayusculas, 
2 minusculas y 4 numeros
'''

def mostrar_juegos(dic):
    for j, datos in dic.items():
        print(j, datos)

def valida_code(code):
    Mayuscula=0
    Minuscula=0
    Numero=0
    for c in code:
        if c.isupper():
            Mayuscula+=1
        if c.islower():
            Minuscula+=1
        if c.isdigit():
            Numero+=1
    if Mayuscula==2 and Minuscula==2 and Numero==4:
        print('El codigo que ingreso es valido')
        return True
    else:
        print('El codigo que ingreso no es valido')
        return False

valida_code('BCaa2024')

# while True:
#     op=int(input('''
#                 1.- Agregar juego
#                 2.- Borrar juego
#                 3.- Actualizar juego
#                 4.- Mostrar catalogo de juegos
#                 5.- Salir
#                  '''))
#     match op:
#         case 1:
#             nombre=input('Ingrese el nombre del juego: ')
#             precio=int(input('Ingrese el precio: '))
#             code=input('Ingrese el codigo: ')
#             largo=len(juegos)
#             if valida_code(code):
#                 juegos[largo+1]={
#                             'nombre': nombre,
#                             'precio': precio,
#                             'code': code
#                         }
#             else:
#                 print('El codigo es invalido, porfavor intente de nuevo')
#             for j, datos in juegos.items():
#                 print(j, datos)
#         case 2:
#             mostrar_juegos(juegos)
#             borrar=int(input('Que juego desea borrar?: '))
#             del juegos[borrar]
#         case 3:
#             mostrar_juegos(juegos)
#             act=int(input('Qe juego desea actualizar?: '))
            
#         case 4:
#             mostrar_juegos(juegos)
#         case _:
#             print('Ingrese una opcion valida')
