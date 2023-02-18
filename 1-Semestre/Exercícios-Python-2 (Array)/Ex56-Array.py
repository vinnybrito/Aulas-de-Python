# 56- Armazenar o nome e idade de cem pessoas. Após a digitação,
# exibir os dados (nome e idade) de todas as pessoas.

nome = []
idade = []

for i in range(0, 3, 1):
    nome.append(input("Insira o nome: "))

    idade.append(int(input("Digite a idade: ")))

for i in range(0, 3, 1):
    print(f"{nome[i]} tem {idade[i]} anos.")
