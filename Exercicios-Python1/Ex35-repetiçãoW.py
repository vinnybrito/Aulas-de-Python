
v = int(input('Digite um valor qualquer: '))

while (v < 0):
    print('Números negativos não são permitidos!')
    v = int(input('Por favor, digite novamente: '))

i = 1

while (i <= 10):
    r = v * i 
    print(f'{v} X {i} = {r}')
    i = i + 1
