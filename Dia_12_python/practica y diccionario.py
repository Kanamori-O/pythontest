'''
 Tarea
 Crear programa de manejo de notas
 1.- Ingresar nota
 2.- Borrar nota
 3.- Mostrar notas
 4.- Sacar promedio, nota mayor y nota menot
 5.- Limpiar todas las notas
 6.- Salir
 '''
notas=[3.1, 7.0, 5.6]
# while True:
    # op=int(input('''
    #     Selecciona una opcion
    #     1.- Ingresar nota
    #     2.- Borrar nota
    #     3.- Mostrar notas
    #     4.- Sacar promedio, nota mayor y nota menor
    #     5.- Limpiar todas las notas
    #     6.- Salir
    #     '''))
    # match op:
    #     case 1:
    #         while True:
    #             try:
    #                 nota=float(input('Ingrese una nota: '))
    #                 notas.append(nota)
    #                 print(notas)
    #                 break
    #             except Exception:
    #                 print('Ponga un numero valido')
    #     case 2:
    #         while True:
    #             try:
    #                 print(notas)
    #                 rm_nota=float(input('Ingrese la nota a remover: '))
    #                 notas.remove(rm_nota)
    #                 print(notas)
    #                 break
    #             except Exception:
    #                 print('Ponga un numero valido')
    #     case 3:
    #         for nota in notas:
    #             print(nota)
    #     case 4:
    #         prom=0
    #         div=0
    #         for i in notas:
    #             # print(i)
    #             prom+=i
    #         notas.sort()
    #         notas.reverse()
    #         print(f'Su nota mas alta es {notas[0]}')
    #         print(f'Su nota mas baja es {notas[-1]}')
    #         prom/=len(notas)
    #         print('Su promedio es de ', round(prom,1))
    #     case 5:
    #         notas.clear()
    #         print('Acaba de limpiar la lista de calificaciones')
    #     case 6:
    #         print('Saliendo....')
    #         break
    #     case _:
    #         print('Opcion invalida')

# Son conjuntos de pares de datos

dic={
    'nombre': 'David Finch',
    'numero': 5423652,
    'casado':True
}

# print(dic['nombre'])
# 
# for key, value in dic.items():
    # print(key, value)

frutas={
    'Manzana': 1500,
    'Frutilla': 1600,
    'Durazno': 3800
}

print(frutas)

frutas['Pera']=1200

print(frutas)

fru=input('Ingrese una fruta')
val= input('Ingrese el precio')

frutas[fru]=val

'''
Usando diccionarios
1.- Ingresar frutas y precio
2.- Actualizar precio
3.- Borrar Fruta y precio
4.- Mostrar todas las frutas y precios
5.- Salir
'''