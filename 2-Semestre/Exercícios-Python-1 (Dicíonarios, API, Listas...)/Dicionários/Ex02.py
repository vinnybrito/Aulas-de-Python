# 2- Crie um programa para cadastrar produtos (nome, preço, quantidade) e pergunte para 
# cada produto em quais lojas ele será comercializado. Caso o produto seja 
# comercializado em lojas, permita ele cadastrar os dados das lojas (nome, cidade). 
# Ao final, exibir todos os produtos e suas respectivas lojas, se houver.

produtos = []

while True:
    print('\n<<------Cadastro de Produtos------>>')
    print('Digite os dados do produto: ')

    nome = input('\nProduto: ')
    preco = float(input('Preço: '))
    quantidade = int(input('Quantidade: '))

    resposta = input('\nO produto cadastrado é comercializado em lojas? (S/N) ')

    if (resposta.upper() == 'S'):
        loja = input('Nome da Loja: ')
        cidade = input('Cidade: ')

        estabelecimento = {'loja': loja, 'cidade': cidade} 
        print('\nProduto Cadastrado com Sucesso!')
    else:
        estabelecimento = {}
        print('\nProduto Cadastrado com Sucesso!')
    
    dado = {'nome': nome, 'preco': preco, 'quantidade': quantidade, 'estabelecimento': estabelecimento}

    produtos.append(dado)

    continuar = input("\nDeseja continuar? (S/N) ")
    if continuar.upper() == "N":
        break

for dado in produtos:
    print(f"\nProduto: {dado['nome']} | Preço: {dado['preco']} | Quantidade: {dado['quantidade']} ")

    if (estabelecimento):
        print(f"Loja: {estabelecimento['loja']} | Cidade: {estabelecimento['cidade']} ")
    else:
        print('Produto não é comercializado em outros estabelecimentos.')