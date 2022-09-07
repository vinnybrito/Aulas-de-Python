
n = 5
i = 1

while(n <= 0):
    print("Não pode numero negativo!")
    num = int(input("Digite um outro numero para obter a tabuada: "))

while(i < 11):
    r = n * i
    print(f'{n} X {i} = {r}')
    i = i + 1
