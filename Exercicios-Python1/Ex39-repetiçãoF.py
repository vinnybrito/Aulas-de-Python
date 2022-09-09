
n = 1
n1 = 0
n2 = 1
n3 = 2

print(f'1 : {n}')

for n3 in range(2, 31):
    a = n1 + n2
    print(f'{n3} : {a}')
    n1 = n2
    n2 = a
    n3 = n3 + 1
