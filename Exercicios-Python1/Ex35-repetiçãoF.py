
v = int(input('Digite o valor que será multiplicado: '))

while (v < 0):
    print('Números negativos não são permitidos!')
    v = int(input('Por favor, digite novamente: '))

i = 1

for i in range(1, 11, 1):
    r = v * i
    print(f'{v} X {i} = {r}')
