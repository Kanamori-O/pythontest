pikaroll=0
otakroll=0
squidroll=0
eelroll=0
pedido=0
pika=0
otaku=0
squid=0
eel=0

while True:
    try:
        op=int(input('''Que es lo que desea hacer
                     1. Elegir Rolls
                     2. Ver carrito
                     3. Pagar
                     4. Salir 
                     '''))
        match op:
            # Rolls
            case 1:
                while True:
                    rolls=int(input('''Seleccione una opcion
                                     1. Pikachu Roll = $4.500
                                     2. Otaku Roll = $5.000
                                     3. Pulpo Venenoso Roll = $ 5200
                                     4. Anguila Eléctrica Roll = $4800
                                     5. Salir
                                     '''))
                    # Seleccion de rolls
                    match rolls:
                        case 1:
                            pedido+=4500
                            pika+=1
                            print(f'Carrito: {pedido}')
                        case 2:
                            pedido+=5000
                            otaku+=1
                            print(f'Carrito: {pedido}')
                        case 3:
                            pedido+=5200
                            squid+=1
                            print(f'Carrito: {pedido}')
                        case 4:
                            pedido+=4800
                            eel+=1
                            print(f'Carrito: {pedido}')
                        case 5:
                            break
            # Carrito
            case 2:
                print(f'Pikachu Roll ({pika}) = $4.500 c/u')
                print(f'Otaku Roll ({otaku}) = $5.000 c/u')    
                print(f'Pulpo Venenoso Roll ({squid}) = $5200 c/u')
                print(f'Anguila Eléctrica Roll ({eel}) = $4800 c/u')    
                print(f'Total {pedido}')
                carrito=int(input('''Que es lo que desea hacer: 
                                  1. Remover un articulo
                                  2. Pagar
                                  3. Salir
                                  '''))
                match carrito:
                    # Remover rolls
                    case 1:
                        pedido=int(input(f'''Seleccione una opcion
                                         1. Pikachu Roll ({pika}) = $4.500
                                         2. Otaku Roll ({otaku}) = $5.000
                                         3. Pulpo Venenoso Roll ({squid}) = $5200
                                         4. Anguila Eléctrica Roll ({eel}) = $4800
                                         5. Salir
                                         '''))    
                        match pedido:
                                case 1:
                                    pedido-=4500
                                    pika-=1
                                    print(f'Carrito: {pedido}')
                                case 2:
                                    pedido-=5000
                                    otaku-=1
                                    print(f'Carrito: {pedido}')
                                case 3:
                                    pedido-=5200
                                    squid-=1
                                    print(f'Carrito: {pedido}')
                                case 4:
                                    pedido-=4800
                                    eel=1
                                    print(f'Carrito: {pedido}')
                                case 5:
                                    break
                    # Pagar
                    case 2:
                        resp=int(input('''Tiene cupon de descuento?
                                      1. Si
                                      2. No
                                      '''))
                        if resp==1:
                            codigoDesc=input('Ingrese el cupon ')
                            if codigoDesc=='soyotaku':
                                total_productos=pika+otaku+squid+eel
                                total=pikaroll+otakroll+squidroll+eelroll
                                desc=total*0.1
                                total_desc=total-desc
                                print('*************************')
                                print(f'TOTAL PRODUCTOS: {total_productos}')
                                print('*************************')
                                print(f'Pikachu Roll : {pika}')
                                print(f'Otaku Roll : {otaku}')
                                print(f'Pulpo Venenoso Roll : {squid}')
                                print(f'Anguila Eléctrica Roll : {eel}')
                                print('*************************')
                                print(f'Subtotal por pagar: ${total}')
                                print(f'Descuento por codigo: ${desc}')
                                print(f'TOTAL: ${total_desc}')
                                break
                            else:
                                print('El cupon es invalido')
                        elif resp==2:
                                    total_productos=pika+otaku+squid+eel
                                    total=pikaroll+otakroll+squidroll+eelroll
                                    print('*************************')
                                    print(f'TOTAL PRODUCTOS: {total_productos}')
                                    print('*************************')
                                    print(f'Pikachu Roll : {pika}')
                                    print(f'Otaku Roll : {otaku}')
                                    print(f'Pulpo Venenoso Roll : {squid}')
                                    print(f'Anguila Eléctrica Roll : {eel}')
                                    print('*************************')
                                    print(f'Subtotal por pagar: ${total}')
                                    print(f'TOTAL: ${total}')
                                    break
                    # Salir
                    case 3:
                          break
            # Pagar
            case 3:  
                  resp=int(input('''Tiene cupon de descuento?
                                      1. Si
                                      2. No
                                      '''))
                  if resp==1:
                            codigoDesc=input('Ingrese el cupon ')
                            if codigoDesc=='soyotaku':
                                total_productos=pika+otaku+squid+eel
                                total=pikaroll+otakroll+squidroll+eelroll
                                desc=total*0.1
                                total_desc=total-desc
                                print('*************************')
                                print(f'TOTAL PRODUCTOS: {total_productos}')
                                print('*************************')
                                print(f'Pikachu Roll : {pika}')
                                print(f'Otaku Roll : {otaku}')
                                print(f'Pulpo Venenoso Roll : {squid}')
                                print(f'Anguila Eléctrica Roll : {eel}')
                                print('*************************')
                                print(f'Subtotal por pagar: ${total}')
                                print(f'Descuento por codigo: ${desc}')
                                print(f'TOTAL: ${total_desc}')
                                break
                            else:
                                print('El cupon es invalido')
                  elif resp==2:
                                    total_productos=pika+otaku+squid+eel
                                    total=pikaroll+otakroll+squidroll+eelroll
                                    print('*************************')
                                    print(f'TOTAL PRODUCTOS: {total_productos}')
                                    print('*************************')
                                    print(f'Pikachu Roll : {pika}')
                                    print(f'Otaku Roll : {otaku}')
                                    print(f'Pulpo Venenoso Roll : {squid}')
                                    print(f'Anguila Eléctrica Roll : {eel}')
                                    print('*************************')
                                    print(f'Subtotal por pagar: ${total}')
                                    print(f'TOTAL: ${total}')
                                    break
            # Salir
            case 4:
                  break
    except Exception:
         print('Opcion invalida, porfavor escriba una de las opciones disponibles')
print('Gracias por su compra')