# 66- Armazenar seis valores em uma matriz de ordem 3x2. Apresentar os valores na tela

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3, 1):
    for c in range(0, 3, 1):
        matriz[l][c] = int(input('Digite um número: '))

for i in range(0, 3, 1):
    print(matriz[i])
