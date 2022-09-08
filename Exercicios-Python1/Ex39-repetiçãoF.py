
v = 30
n1 = 1
n2 = 1
n3 = 3

print(f'1 : {n1}')
print(f'2 : {n2}')

for n3 in range(1, 31):
    a = n1 + n2
    print(f'{n2} : {a}')
    n1 = n2
    n2 = a
    n3 = n3 + 1
