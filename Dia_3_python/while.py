# # uso y explicacion de while

# import time
# num=10

# while num>=0:
#     print(num)
#     time.sleep(1)
#     num-=1

# resp='no'

# while resp !='si':
#     resp=input('Desea salir del sistema?')

clave=3344
constraseña=int(input('Ingrese su constraseña'))
while clave!=constraseña:
    print('ERROR; clave invalida')
    constraseña=int(input('Ingrese su constraseña'))
print('Bienvenido al sistema')