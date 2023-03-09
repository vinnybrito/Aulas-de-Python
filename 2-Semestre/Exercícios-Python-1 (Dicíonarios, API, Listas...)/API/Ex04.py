# 4- Crie um programa em Python que permita cadastrar pessoas e seu respectivo endereço. # Ao cadastrar o endereço deixe a pessoa, digitar apenas o cep e o restante dos campos, # deve ser completado de acordo com o retorno da API, como rua, bairro, cidade e estado. # A pessoa, só deve cadastrar seu nome, email, número da casa e complemento.
# Todo esse conteúdo deve ser cadastrado em um Dicionário. O programa deve permitir, 
# Incluir, Alterar, Excluir e Consultar Pessoas.

import requests

listaPessoas = []

while True:

    print('\n//---------Cadastro de Pessoas---------//')
    print('\nEscolha uma opção: \n1- Incluir \n2- Alterar \n3- Excluir \n4- Consultar \n5- Sair')

    opcao = int(input('\nOpção desejada: '))

    if (opcao == 1):

        id = listaPessoas.__len__() + 1
        nome = input('\nDigite o seu nome: ')
        email = input('Digite o seu E-mail: ')
        cep = input('Digite seu CEP: ')

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

            pessoa = {"id": id, "nome": nome, "email": email, "logradouro": rua, "bairro": bairro, "localidade": localidade, "uf": uf, "numero": numero, "complemento": complemento }

            listaPessoas.append(pessoa)

            print('Pessoa cadastrada com sucesso!')
        else:
            print("CEP não encontrado.")
    elif (opcao == 2):
        for pessoa in listaPessoas:
            print(f"\n\nId: {pessoa['id']} \nNome: {pessoa['nome']} \nEndereço: {pessoa['logradouro']}\n\n")

        idPessoa = int(input('Digite o id da pessoa que deseja atualizar: '))
        nome = input('Digite o novo nome: ')
        email = input('Digite o novo email: ')

        for pessoa in listaPessoas:
            if (pessoa['id'] == idPessoa):
                pessoa.update({'nome': nome})
                pessoa.update({'email': email})

        print('Pessoa atualizada com sucesso!')
    elif (opcao == 3):
        for pessoa in listaPessoas:
            print(f"\n\nId: {pessoa['id']} \nNome: {pessoa['nome']} \nEndereço: {pessoa['logradouro']}\n\n")

        idPessoa = int(input('Digite o id da pessoa que deseja atualizar: '))

        for pessoa in listaPessoas:
            if (pessoa['id'] == idPessoa):
                listaPessoas.remove(pessoa)
    elif (opcao == 4):     
        for pessoa in listaPessoas:
            print(f"\n\nId: {pessoa['id']} \nNome: {pessoa['nome']} \nEndereço: {pessoa['logradouro']}\n\n")
    elif (opcao == 5):
        break
print("\nSistema de cadastro encerrado. Tchau!")
