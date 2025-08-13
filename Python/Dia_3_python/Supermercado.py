cant=int(input('Cuantos productos llevara?'))
total=0
for i in range (cant):
    print('''
    Que producto llevará?
	1.- Diazepam $9000
	2.- Metametozona $18500
	3.- Oblea China $1000" ''')
    op=int(input())
    if op==1:
        print('Usted llevara Diazepam')
        total=total+9000
    elif op==2:
        print('Usted llevo Metametazona')
        total=total+18500
    elif op==3:
        print('Usted llevo Oblea China')
        total=total+1000
    else:
        print('Opcion no valida')
iva=total*1.19
print('Su total neto es', total)
print('El total mas IVA es', total*1.19)
