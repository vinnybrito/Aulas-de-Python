i = 1
j = 1

while(i <= 20):
    while(j <= 10):
        t = i * j
        print(f'{i} X {j} = {t}')
        j = j +1
    j = 1
    i = i + 1
    input('Digite qualquer tecla para continuar...')
    