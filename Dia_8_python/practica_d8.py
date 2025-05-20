import random

# # Perros de caza
# # Pida al usuario la cantidad de perros
# # Muestre cual es la cuota minima de conejos
# # luego consulte cuantos conejos trajo
# # si el perro trajo la cantidad minima
# # cumplio la cuota, sino, se queda sin filete
# # mostrar resumen de perro que cumplieron y los que no 

# while True:
#     try:
#         cuota=random.randint(1,5)
#         dog_count=0
#         filete=0
#         hambre=0
#         dog=int(input('Cuantos perros van a ir a cazar?'))
#         while dog<1:
#             print('Debe ingresar al menos un perro')
#             dog=int(input('Cuantos perros van a ir a cazar?'))
#         print(f'La cuota de conejos es de {cuota}')
#         for i in range(dog):
#             bnny=random.randint(0,5)
#             dog_count+=1
#             if bnny>=cuota:
#                 print(f'El perro {dog_count} trajo {bnny} por ende se gano el filete 👑')
#                 filete+=1
#             else:
#                 print(f'El perro {dog_count} trajo {bnny} por ende va a pasar hambre esta noche 💀')
#                 hambre+=1
#         print(f'Los perros que lograron la cuota son {filete} y los que no son {hambre}')
#     except Exception:
#         print('Solo debe ingresar numeros enteros')

# Quiere pasar el ramo?
# Pregunte la cantidad de rojos en el curso
# Los talleres que hay en el semestre son 4
# Por cada taller asistido obtiene 0.3 decimas
# Si el alumno tiene mas de 1 punto
# tiene la bendicion del profesor
# si no, no se le puede ayudar
# Ingrese la nota final y sume las decimas acumuladas 
# Muestre si aprueba o reprueba.

alumnos=int(input('Ingrese la cantidad de rojos que tiene el curso'))
for i in range(alumnos):
    decimas=0
    rojos=random.randint(1.0, 3,9)
    print(rojos)
    taller=random.randint(0, 4)
    print(taller)
    if taller==1:
        decimas+=0.3
    elif taller==2:
        decimas+=0.6
    elif taller==3:
        decimas+=0.6

print(decimas)

