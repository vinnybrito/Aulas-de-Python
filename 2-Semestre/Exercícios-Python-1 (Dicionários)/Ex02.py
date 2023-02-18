# Crie um programa para cadastrar produtos (nome, preço, quantidade) e pergunte para 
# cada produto em quais lojas ele será comercializado. Caso o produto seja 
# comercializado em lojas, permita ele cadastrar os dados das lojas (nome, cidade). 
# Ao final, exibir todos os produtos e suas respectivas lojas, se houver.

produtos = []

while True:
    nome = input("Digite o nome: ")
    preco = int(input("Digite a preço: "))
    quantidade = int(input("Digite a quantidade: "))

    comercios = input("O produto é comercializado?? (S/N): ")
    if (comercios.upper() == "S"):
        n = input("Digite nome do estabelecimento: ")
        cidade = input("Digite a cidade:")

        comer = {"nome": nome, "cidade": cidade}
    else:
        comer = {}

    tiposproduto = {"nome": nome, "preco": preco, "quantidade": quantidade, "loja": comer}

    produtos.append(tiposproduto)

    continuar = input("Deseja continuar? (S/N) ")
    if continuar.upper() == "N":
        break

for tiposproduto in produtos:
    print(f"Nome: {tiposproduto['nome']} | Preço: {tiposproduto['preco']} | Quantidade: {tiposproduto['quantidade']}")



