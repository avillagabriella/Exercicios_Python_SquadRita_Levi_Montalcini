lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do segundo lado: '))

ehTriangulo = False

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    ehTriangulo = True

if (ehTriangulo):
    if lado1 == lado2 and lado2 == lado3:
        print('O triângulo é equilatero!')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('O triângulo é escaleno!')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('O triângulo é isosceles!')
else:
    print('Não é um triângulo!')