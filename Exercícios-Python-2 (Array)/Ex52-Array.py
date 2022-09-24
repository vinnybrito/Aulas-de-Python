
n = []

for i in range(0, 10, 1):
    n.append(int(input('Digite um valor: ')))

m = n[0]

for i in range(0, 10, 1):
    if (n[i] > m):
        m = n[i]

print('O maior número do Array é: ', m)
