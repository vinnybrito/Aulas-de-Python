s = 0
i = 1

while (i <= 10):
    n = int(input('Digite um valor: '))

    if (i == 1):
        m = n
        i = i + 1
    elif(n > m):
        i = i + 1
        m = n

    s = s + n

md = s / 10

print('O maior valor é ', m)
print('A soma é ', s)
print('A média é ', md)