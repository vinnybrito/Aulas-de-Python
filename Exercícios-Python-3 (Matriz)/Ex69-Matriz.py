# 69- Entrar via teclado com doze valores e armazená-los em uma matriz de ordem 3x4. 
# Após a digitação dos valores solicitar uma constante multiplicativa, que deverá 
# multiplicar cada valor matriz e armazenar o resultado em outra matriz de mesma ordem, 
# nas posições correspondentes. Exibir as matrizes na tela, sob a forma matricial, ou 
# seja, linhas por colunas.

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matriz2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        matriz[l][c] = int(input('Digite um número: '))

constante = int(input("Digite o valor a ser multiplicado: "))

for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        matriz2[l][c] = matriz[l][c] * constante

print('\nPrimeira Matriz:')
for i in range(0, 3, 1):
    print(matriz2[i])

print('\nSegunda Matriz:')
for i in range(0, 3, 1):
    print(matriz2[i])