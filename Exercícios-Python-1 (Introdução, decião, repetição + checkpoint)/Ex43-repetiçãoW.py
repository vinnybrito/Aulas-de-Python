n = int(input("Digite um valor positivo menor que 50: "))

while (n <= 0 or n > 50):
    print("Valor invalido!")
    n=int(input("Digite um valor positivo menor que 50: "))
i = 0
while(i <= n):
    if(i == 0):
        a = ((i + 1)*(i + 1)) + 1
        b = (i + 1) **3
        x = (a/b)
    else:
        x = x + ((((i + 1) * (i + 1)) + 1)/((i + 1) **3))
        print(f"O {i}º valor é:",x)
    i =  i + 1