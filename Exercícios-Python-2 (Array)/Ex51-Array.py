
num = []

for i in range(0, 10, 1):
    num.append(int(input('Digite um valor: ')))

print('Os números que você digitou foram: ')

for i in range(9, -1, -1):
    print(num[i])
