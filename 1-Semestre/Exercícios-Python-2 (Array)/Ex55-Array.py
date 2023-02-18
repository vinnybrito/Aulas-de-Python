# 55- Armazenar um máximo de 20 valores em um vetor. A quantidade de valores a serem
# armazenados será escolhida pelo usuário. Enviar mensagem de erro, caso 
# a quantidade de valores escolhida esteja fora da faixa possível e solicitar a
# quantidade novamente. Após a digitação dos valores, criar uma rotina de consulta,
# onde o usuário digita um número e o programa exibe em qual posição do vetor este 
# número está localizado. Se o número não for encontrado, enviar mensagem “Valor não 
# encontrado!”. Perguntar ao usuário se deseja ou não fazer uma nova consulta, 
# consistir a resposta e encerrar o programa em caso negativo.

n = []
posicao = -1
novamente = 's'

a = int(input("Digite a quantidade de valores a serem digitados: "))

while (a <= 0 or a > 5):
    a = int(input("Digite novamente a quantidade de valores: "))

for i in range(0, a, 1):
    n.append(int(input("Digite um valor: ")))

while (novamente == 's'):

    num = int(input("Digite um número para ser localizado no Array: "))

    for i in range(0, a, 1):
        if(n[i] == num):
            posicao = i

    if (posicao != -1):
        print("O valor foi encontrado na posição ", posicao)
    else:
        print("Valor não encontrado!")

    novamente = input("Deseja realizaer uma nova consulta?: ")

print("Obrigado!")