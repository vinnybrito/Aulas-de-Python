v = int(input('Digite o valor a ser multiplicado: '))

while (v < 0):
    v = int(input('Valores negativos não são permitidos.\nDigite novamente: '))

i = 1

while (i <= 10):
    r = v * i 
    print(f'{v} X {i} = {r}')
    i = i + 1