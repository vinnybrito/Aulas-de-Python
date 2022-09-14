a = 1
b = 2
x = a / b

n = int(input("Digite um valor positivo menor que 50: "))

while(n <= 0 or n > 50):
    print("Valor invalido!")
    n = int(input("Digite um valor positivo menor que 50: "))

for i in range(1, n+1 ,1):
    a = a + 1
    b = b + 1
    x = x + (a/b)
    print(f"O {i}º valor é:", x)