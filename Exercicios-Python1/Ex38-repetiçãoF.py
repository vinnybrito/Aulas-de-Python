
v = int(input('Digite um valor qualquer: '))

while (v < 0):
    v = int(input('Por favor, digite novamente: '))

i = 1

for i in range(1, 101, 1):
    r = v + i 
    print(f'{v} + {i} = {r}')
