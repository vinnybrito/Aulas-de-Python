# 53- Armazenar vinte valores em um vetor. Após a digitação, 
# entrar com uma constante multiplicativa que deverá multiplicar 
# cada um dos valores do vetor e armazenar o resultado no próprio vetor, 
# na respectiva posição.

n = []

for i in range(0, 5, 1):
    n.append(int(input("Digite um valor: ")))

constante = int(input("Digite um valor que multiplicará os anteriores: "))

for i in range(0, 5, 1):
    n[i] = n[i] * constante
    print(n[i])