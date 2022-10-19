# 23- Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A 
# + B é menor que C.

a = int(input('Digite o primeiro valor: '))

b = int(input('Digite o segundo valor: '))

c = int(input('Digite o terceiro valor: '))

if (a + b < c):
    print(f'A soma dos dois primeiros números é menor que {c}.')
else:
    print(f'A soma dos dois primeiros números é maior que {c}.')
