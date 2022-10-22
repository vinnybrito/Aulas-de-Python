# 68- Entrar via teclado com doze valores e armazená-los em uma matriz de ordem 3x4. Após 
# a digitação dos valores solicitar uma constante multiplicativa, que deverá multiplicar 
# cada valor matriz e armazenar o resultado na própria matriz, nas posições correspondentes.

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        matriz[l][c] = int(input('Digite um número: '))

constante = int(input("Digite o valor que realizará a multiplicação: "))

for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        matriz[l][c] = matriz[l][c] * constante

for i in range(0, 3, 1):
    print(matriz[i])