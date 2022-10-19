# 16- Verificar se três valores quaisquer (A, B, C) que serão digitados formam ou não um triângulo retângulo. Lembre-se que o quadrado da hipotenusa é igual a soma dos quadrados dos catetos.

h = int(input('Digite o valor da Hipotenusa: '))

ca = int(input('Digite o valor do primeiro catato: '))

co = int(input('Digite o valor do segundo cateto: '))

if (h * h) == (ca * ca) + (co * co):
    print('É um triângulo retângulo.')
else:
    print('Não é um triângulo retângulo.')
