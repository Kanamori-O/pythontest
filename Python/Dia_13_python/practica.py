import random

def suma():
    n1=int(input('Ingrese un numero'))
    n2=int(input('Ingrese otro numero'))
    print(n1+n2)
def suma_arg(n1, n2):
    print(n1+n2)
def suma_ret():
    n1=int(input('Ingrese un numero'))
    n2=int(input('Ingrese otro numero'))
    return n1+n2
def suma_arg_return(n1, n2):
    return n1+n2
def resta_arg(n1, n2):
    print(n1-n2)

# suma()
# suma_arg(7, 9)
# resta_arg(6,10)
# print(suma_ret())
# print(suma_arg_return(10, 40))

'''
-Realizar una funcion que calcule el IVA

-Realizar otra funcion que al pasarle un precio
 y un numero como porcentaje (ej 20)
 calcule el descuento y muestre el valor final
'''

def iva(n1):
    # n1=int(input('ingrese un numero '))
    return n1*0.19
neto=500
# print('El IVA es', iva(neto))
# print('El precio total es', iva(neto)+neto)
def porcentaje():
    n1=int(input('Ingrese un precio'))
    n2=int(input('Ingrese el porcentaje'))
    return n1/100*n2
# print(porcentaje())

productos=[
    {'nombre':'lapiz', 'precio': 400},
    {'nombre':'goma', 'precio': 200},
    {'nombre':'estuche', 'precio': 1600}
]
# for producto in productos:
    # print('El precio del articulo', producto['nombre'], 'es:', producto['precio'])

'''
1.- Agregar articulo
2.- Borrar articulo
3.- Actualizar articulo
4.- Mostrar listado de articulos
5.- Salir
'''

while True:
    op=int(input(
        '''
        1.- Agregar articulo
        2.- Borrar articulo
        3.- Actualizar articulo
        4.- Mostrar listado de articulos
        5.- Salir
        '''))
    match op:
        case 1:
            articulo=input('Agregue un articulo ')
            precio=int(input('Ingrese el valor del articulo '))
            productos.insert(0,{'nombre':articulo, 'precio':precio})
        case 2:
            for n,producto in enumerate(productos):
                print(n+1, producto['nombre'], producto['precio'])
            rm_producto=int(input('Ingrese el producto a remover '))
            productos.pop(rm_producto-1)
        case 3:
            for n,producto in enumerate(productos):
                print(n+1, producto['nombre'], producto['precio'])
            num_artic=int(input('Ingrese el ID'))
            articulo=input('Actualice el nombre de un articulo')
            precio=int(input('Actualice el valor del articulo'))
            productos[num_artic-1]['nombre']=articulo
            productos[num_artic-1]['precio']=precio
        case 4:
            for n,producto in enumerate(productos):
                print(n+1, producto['nombre'], producto['precio'])
        case 5:
            print('Saliendo...')
            break
        case _:
            print('Opcion invalida')