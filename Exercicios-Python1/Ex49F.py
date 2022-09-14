inicial = int(input('Digite o valor inicial: '))

final = int(input('Digite o valor final: '))

s = 0
i = 1

for i in range(inicial, final + 1, 1):
    s = s + i
print(s)