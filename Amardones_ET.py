
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}
 
def stock_marca(marca):
    c_marca=input('Ingrese marca a consultar: ')
    for cantidad in productos:
        print(cantidad)

def busqueda_precio(bprecio):
    p_min=int(input('Ingrese precio mínimo: '))
    p_max=int(input('Ingrese precio máximo: '))
    for producto in productos:
        if producto>='productos':
            print(stock(producto))

def actualizar_precio(modelo, p):
    m_actualizar=input('Ingrese modelo a actualizar:')
    p_actualizar=int(input('Ingrese precio nuevo: '))
    stock.update()=m_actualizar, [0]=p_actualizar

while True:
    op=int(input('''
                *** MENU PRINCIPAL ***
                1. Stock marca.
                2. Búsqueda por precio.
                3. Actualizar precio
                4. Salir
                '''))
    match op:
        case 1:
            stock_marca(stock)
        case 2:
            busqueda_precio(productos)
        case 3:
            actualizar_precio()
        case 4:
            print('Programa finalizado.')
            break
        case _:
            print('Debe seleccionar una opción válida!!')