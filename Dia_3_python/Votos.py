cant=int(input('Ingrese el numero de votantes'))
kaiser=0
putin=0
for i in range(cant):
    print(''''
    Ingrese su voto:
    1.- Kaiser
    2.- Putin''')
    op=int(input())
    if op==1:
        print('Usted voto por Kaiser')
        kaiser=kaiser+1
    elif op==2:
        print('Usted voto por Putin')
        putin=putin+1
    else:
        print('Voto invalido')
if kaiser>putin:
    print('Gano Putin con una cantidad de votos de', putin)
else:
    print('Gano Kaiser con una cantidad de votos de', kaiser)
