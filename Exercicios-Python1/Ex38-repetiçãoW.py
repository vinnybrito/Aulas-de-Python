
v = int(input('Digite um valor qualquer: '))

while (v < 0):
    v = int(input('Por favor, digite novamente: '))

i = 1

while (i <= 100):
    r = v + i 
    print(f'{v} + {i} = {r}')
    i = i + 1
