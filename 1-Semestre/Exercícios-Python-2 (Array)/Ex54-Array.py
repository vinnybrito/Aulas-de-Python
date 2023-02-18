# 54- Armazenar vinte valores na memória. Após a digitação, entrar com uma constante
# multiplicativa que deverá multiplicar cada um dos valores do vetor e armazenar o
# resultado em outro vetor, porém em posições equivalentes. Exibir os vetores 
# na tela.

n = []
resultado = []

for i in range(0, 5, 1):
    n.append(int(input("Digite um valor: ")))

constante = int(input("Digite um valor que multiplicará os valores anteriores: "))

for i in range(0, 5, 1):
    resultado.append(n[i] * constante)
    print(resultado[i])