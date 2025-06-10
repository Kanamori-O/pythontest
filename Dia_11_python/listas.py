# uso y ejemplo de listas
# que es una lista?
# es una coleccion de datos

#     -8 -7 -6 -5  -4  -3  -2  -1 
numeros=[5, 3, 4, 6, 73, 67, 32, 56]
#      0  1  2  3  4   5   6   7

print(numeros.insert(3, 10))
print(numeros)
numeros.remove(67)
print(numeros)
# numeros.clear()
# print(numeros)
# numeros.reverse()
numeros.sort()
print(numeros)

# print(len(numeros))

# print(f'Lista sin agregar nada {numeros}')

# # index es para ver el indice del elemento
# # print(numeros.index(73))

# numeros.append(346)
# print(f'Lista con un elemento agregado {numeros}')

# for numero in numeros:
#     print(numero)

# num=int(input('Ingrese un numero'))

# numeros.append(num)

# print(numeros)

'''
Ejemplo
'''
# Shigeru, Hideki, Hideo
# Miyamoto, Anno, Kojima

# Shigeru Miyamoto
# Hideki Anno
# Hideo Kojima

# nombres=['Irthur', 'Fresia']
# apellidos=['Kandriel', 'Velmora'] 
# while True:
#     print('''
#         1.- Ingresar nombre
#         2.- Buscar nombre
#         3.- Mostrar lista
#         4.- Salir
#           ''')
#     op=int(input('Seleccione una opcion: '))
#     match op:
#         case 1:
#             nom=input('Ingrese un nombre: ')
#             nombres.append(nom)
#             ape=input('Ingrese un apellido: ')
#             apellidos.append(ape)
#             print(nombres)
#             print(apellidos)
#         case 2:
#             busca=input('Ingrese el nombre a buscar')
#             if busca in nombres:
#                 print(f'El nombre {busca} existe en la lista')
#             else:
#                 print(f'El nombre {busca} NO existe en la lista')
#         case 3:
#             # cont=0
#             # # for nombre, apellido in zip(nombres, apellidos):
#             # #     print(f'Nombre {cont}: {nombre} {apellido}')
#             # for nombre in nombres:
#             #     print(cont+1, '.-', nombres[cont], '', apellidos[cont])
#             #     cont+=1
#             for i in range(len(nombres)):
#                 print(i+1, '.-', nombres[i], '', apellidos[i])
# #       break
#         case 4:
#             print('Saliendo...')
#             break
# #       error
#         case _:
#             print('Opcion no valida')


'''
Crear carrito 3.0
Tomar el carrito de compras anterior y hacerlo con listas
1.- Ingresar productos
2.- Comprar 
3.- Crear boleta
4.- Salir
Que el carrito comience con 3 productos
Hay que hacer 3 listas, productos, precios y carrito
'''