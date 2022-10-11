#57- Armazenar o nome, sexo e idade de cem pessoas. Consistir as entradas no sentido de aceitar apenas “F” ou “M” para o sexo e valores positivos para a idade. Após a digitação dos dados, exibir os dados (nome, sexo e idade) de todas as pessoas do sexo feminino.

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

for i in range(0, 3, 1):
    if(sexo[i] == "f"):
        print(f"Nome: {nome[i]}, Sexo: {sexo[i]}, Idade: {idade[i]}")