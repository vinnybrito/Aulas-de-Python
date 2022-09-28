#popular um array significa colocar uma coisa lá
#varrer significa percorrer o array

n = []
c = []

for i in range(1, 4, 1):
    n.append(int(input(f'Digite o {i} valor: ')))

const = int(input('Digite o valor da constante: '))

for i in range(1, 4, 1):
    c.append(const * n[i])
    print(n[i])

print('Os vetores são: ')
for i in range(1, 4, 1):
    print(c[i])
