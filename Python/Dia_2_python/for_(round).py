# explicacion y uso de for

# num=int(input('Ingrese un numero '))

# for i in range(num):
#     print(i)

# num=int(input('Ingrese un numero '))
# for i in range(10):
#     print(num,'x',i+1 ,'=', (i+1)*num)

cant=int(input('Ingrese el numero de notas '))
suma=0
for i in range (cant):
    print('Ingrese la nota', i+1)
    nota=float(input())
    suma=suma+nota
prom=suma/cant
print('Su promedio es', round(prom,1))
if prom>=4:
    print('Usted aprobo')
else:
    print('Usted es tontito')