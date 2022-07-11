l1 = int(input('primeiro segmento:'))
l2 = int(input('segundo segmento:'))
l3 = int(input('terceiro segmento:'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('PODEM FORMAR UM TRIANGULO!')
    if l1 == l2 == l3:
        print('E é um triangulo equilatero')
    elif l1 != l2 != l3 != l1:
        print('E é um triangulo escaleno ')
    else:
        print("E é um triangulo isosceles")
else:
    print('NÃO PODEM FORMAR UM TRIANGULO!')
