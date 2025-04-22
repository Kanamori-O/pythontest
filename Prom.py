print('Ingrese 3 notas')
n1=float(input(print))
n2=float(input(print('Ingrese la siguiente nota')))
n3=float(input(print('A continuacion su promedio')))
total=(n1+n2+n3)/3
print('Su promedio es', round(total,1))
if total>4:
    print('Usted aprobo')
else:
    print('Usted es tontito')
