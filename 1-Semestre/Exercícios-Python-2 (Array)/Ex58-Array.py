# 58- Armazenar o nome, sexo e idade de cem pessoas. Consistir as entradas no sentido de aceitar apenas “F” ou “M” para o sexo e valores positivos para a idade. Após a digitação, exibir os dados (nome, sexo e idade) de todas as pessoas com idade superior a dezoito anos. Ao final da lista, exibir a quantidade de pessoas listadas.

nome = []
sexo = []
idade = []

for i in range(0, 3, 1):
    nome.append(input("Digite seu nome: "))

    sex = input("Digite o seu sexo: ")
    while ((sex != "f") and (sex != "m")):
        sex = input("Digite o seu sexo: ")
    sexo.append(sex)

    anos = int(input("Digite sua idade: "))
    while (anos <= 0):
        anos = int(input("Digite sua idade: "))
    idade.append(anos)

j = 0

for i in range(0, 3, 1):
    if(idade[i] >= 18):
        print(f"Nome: {nome[i]}, Sexo: {sexo[i]}, Idade: {idade[i]}")
        j = j + 1

print(j)