
v = int(input('Digite um valor positivo para ser somado: '))

while (v < 0):
    v = int(input('Valores negativos não são permitido.\nDigite novamente: '))

i = 1

for i in range(1, 101, 1):
    r = v + i 
    print(f'{v} + {i} = {r}')
