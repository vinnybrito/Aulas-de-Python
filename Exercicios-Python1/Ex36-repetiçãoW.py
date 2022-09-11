x = int(input('Digite o valor a ser multiplicado: '))

while (x < 0):
    print('Números negativos não são permitidos.')
    x = int(input('Por favor, digite novamente: '))

a = int(input('Digite a quantidade minima de vezes que esse valor vai ser multiplicado: '))

b = int(input('Digite a quantidade máxima de vezes que esse valor vai ser multiplicado: '))

while (a > b):
    b = int(input('O segundo valor precisa ser maior que o primeiro.\nDigite novamente: '))

while (b >= a):
    r = x * b
    print(f'{x} X {b} = {r}')
    b = b - 1