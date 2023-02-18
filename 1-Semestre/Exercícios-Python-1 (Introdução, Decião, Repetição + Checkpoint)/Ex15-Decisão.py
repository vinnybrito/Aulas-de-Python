# 15- A partir de três valores que serão digitados, verificar se formam ou não um 
# triângulo. Em caso positivo, exibir sua classificação: “Isósceles, escaleno ou 
# eqüilátero”. Um triângulo escaleno possui todos os lados diferentes, o isósceles, 
# dois lados iguais e o eqüilátero, todos os lados iguais. Para existir triângulo é 
# necessário que a soma de dois lados quaisquer seja maior que o outro, isto, para
# os três lados.

l1 = float(input('Digite o valor do primeiro lado do triângulo: '))

l2 = float(input('Digite o valor do segundo lado do triângulo: '))

l3 = float(input('Digite o valor do terceiro lado do triângulo: '))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print('É um triângulo.')
    if (l1 == l2) and (l1 == l3):
        print('Triângulo Eqüilatero.')
    elif (l1 != l3) and (l1 != l2):
        print('Triângulo Escaleno.')
    else:
        print('Triângulo Isósceles.')
else:
    print('Não é um Triângulo.')
