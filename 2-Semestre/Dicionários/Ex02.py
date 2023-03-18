# 2- Crie um programa para cadastrar produtos (nome, preço, quantidade) e pergunte para 
# cada produto em quais lojas ele será comercializado. Caso o produto seja 
# comercializado em lojas, permita ele cadastrar os dados das lojas (nome, cidade). 
# Ao final, exibir todos os produtos e suas respectivas lojas, se houver.

produtos = []

while True: 
    print('<<----CADASTRO DE PRODUTOS---->>')

    produto = input('\nProduto: ')
    preco = float(input('Preço: '))
    quantidade = int(input('Quantidade: '))

    resposta = input('\nO produto é comercializado? (S/N): ')

    if (resposta.upper() == "S"):
        loja = input('\nLoja: ')
        cidade = input('Cidade: ')
        comercio = {'loja': loja, 'cidade': cidade}

    mercadoria = {'produto': produto, 'preco': preco, 'quantidade': quantidade, 'comercio': comercio}

    produtos.append(mercadoria)

    continuar = input('\nDeseja continuar? (S/N) ')

    if (continuar.upper() == "N"):
        break

print('\n<<----PRODUTOS CADASTRADOS---->>')

for mercadoria in produtos:
    print(f"\nProduto: {mercadoria['produto']} | Preço: {mercadoria['preco']} | Quantidade: {mercadoria['quantidade']}")
    
    if (comercio):
        print(f"Loja: {comercio['loja']} | Cidade: {comercio['cidade']}")