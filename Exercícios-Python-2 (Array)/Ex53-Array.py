
n = []

for i in range(1, 21, 1):
    n.append(int(input(f'Digite o {i} valor: ')))

const = int(input('Digite o valor a ser multiplicado: '))

for i in range(0, 20, 1):
    n[i] = n[i] * const
    print(n[i])
