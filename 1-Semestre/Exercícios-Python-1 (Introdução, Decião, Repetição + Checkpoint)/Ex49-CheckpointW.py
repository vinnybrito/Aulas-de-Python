inicial = int(input('Digite o valor inicial: '))

final = int(input('Digite o valor final: '))

s = 0
i = 1

while (inicial <= final):
    s = s + inicial
    inicial = inicial + 1
print(s)