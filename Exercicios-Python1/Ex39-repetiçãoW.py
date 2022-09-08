
v = 30
n1 = 0
n2 = 1
n3 = 3

print(f'1 : {n1}')
print(f'2 : {n2}')

while (n3 <= 30):
    a = n1 + n2
    print(f'{n3} : {a}')
    n1 = n2
    n2 = a
    n3 = n3 + 1
