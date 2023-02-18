s = 0

for i in range(1, 11, 1):
    n = int(input('Digite um valor: '))

    if (i == 1):
        m = n
    elif(n > m):
        m = n

    s = s + n

md = s / 10

print('O maior valor é ', m)
print('A soma é ', s)
print('A média é ', md)