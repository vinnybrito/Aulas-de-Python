# 4- Crie um programa em Python que permita cadastrar pessoas e seu respectivo endereço. # Ao cadastrar o endereço deixe a pessoa, digitar apenas o cep e o restante dos campos, # deve ser completado de acordo com o retorno da API, como rua, bairro, cidade e estado. # A pessoa, só deve cadastrar seu nome, email, número da casa e complemento.
# Todo esse conteúdo deve ser cadastrado em um Dicionário. O programa deve permitir, 
# Incluir, Alterar, Excluir e Consultar Pessoas.

import requests

clientes = []

while True: 
    print('\n<<----CADASTRO DE CLIENTES---->>')

    print('\nEscolha uma opção: ')
    print('1- Incluir')
    print('2- Alterar')
    print('3- Excluir')
    print('4- Consultar')
    print('5- Sair')

    opcao = int(input('Opção desejada: '))

    if (opcao == 1):

        id = clientes.__len__() + 1
        nome = input('\nDigite o seu nome: ')
        email = input('Digite seu E-mail: ')
        cep = input('Digite o seu CEP: ')

        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()

            rua = dados['logradouro']
            bairro = dados['bairro']
            localidade = dados['localidade']
            uf = dados['uf']

            numero = input('Número da casa: ')
            complemento = input('Complemento: ')

            pessoa = {'id': id, 'nome': nome, 'email': email, 'cep': cep, 'rua': rua, 'bairro': bairro, 'localidade': localidade, 'cidade': uf, 'numero': numero, 'complemento': complemento}

            clientes.append(pessoa)

            print('\nPessoa cadastrada com sucesso!')

    elif (opcao == 2):
        for pessoa in clientes:      
            print(f"ID: {pessoa['id']} | Nome: {pessoa['nome']}")

        idPessoa = int(input('Digite o id da pessoa que deseja atualizar: '))
        nome = input('Digite o novo nome: ')
        email = input('Digite o novo email: ')

        for pessoa in clientes:
            if (pessoa['id'] == idPessoa):
                pessoa.update({'nome': nome})
                pessoa.update({'email': email})

    elif (opcao == 3):
        for pessoa in clientes:      
            print(f"ID: {pessoa['id']} | Nome: {pessoa['nome']}")
        
        idPessoa = int(input('Digite o id da pessoa que deseja excluir: '))

        for pessoa in clientes:
            if (pessoa['id'] == idPessoa):
                clientes.remove(pessoa)  

    elif (opcao == 4):
        print("\n<<----CLIENTES CADASTRADOS---->>")

        for pessoa in clientes:
            print(f"\nID: {pessoa['id']} | Nome: {pessoa['nome']} | Rua: {pessoa['rua']} | Cidade: {pessoa['cidade']}")
            
    else:
        break

print("\nFim do programa!")