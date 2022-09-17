
num = []

for i in range(0, 10, 1):
    num.append(int(input('Digite um valor: ')))

for i in range(0, 10, 1):
    if num[0] < num[i]:
        num[0] = num[i]

print("O maior número digitado foi:", num[0])