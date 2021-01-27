l1 = float(input('Medida do 1º lado: '))
l2 = float(input('Medida do 2º lado: '))
l3 = float(input('Medida do 3º lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos podem formar um triangulo', end=": ")
    if l1 == l2 == l3:
        print('Equilatero')
    elif l1 != l2 != l3:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Nao podem formar um triangulo')
