from Aluno import Aluno

import requests 

alunos = []

while True:
    print('<<--Cadastro de Alunos-->>')

    print('\nEscolha uma opção:')
    print('1- Incluir Aluno')
    print('2- Alterar')
    print('3- Excluir')
    print('4- Exibir')
    print('5- Sair')

    opcao = int(input('Digite a opção desejada: '))

    if (opcao == 1):
        aluno = Aluno()

        id = alunos.__len__() + 1
        aluno.nome = input('Digite o seu nome: ')
        aluno.idade = input('Digite sua idade: ')
        aluno.ra = input('Digite seu RA: ')
        aluno.curso = input('Digite o nome do curso: ')
        aluno.cep = input('Digite o seu CEP: ')

        url = f"https://viacep.com.br/ws/{aluno.cep}/json/"
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()

            aluno.rua = dados['logradouro']
            aluno.bairro = dados['bairro']
            aluno.localidade = dados['localidade']
            aluno.uf = dados['uf']

            informacoes = {'id': id, 'nome': aluno.nome, 'idade': aluno.idade, 'ra': aluno.ra, 'curso': aluno.curso, 'cep': aluno.cep, 'rua': aluno.rua, 'bairro': aluno.bairro, 'localidade': aluno.localidade, 'cidade': aluno.uf}

            alunos.append(informacoes)
    elif (opcao == 2):
        for informacoes in alunos:      
            print(f"ID: {informacoes['id']} | Nome: {informacoes['nome']}")

        idPessoa = int(input('Digite o id do aluno que deseja atualizar: '))
        nome = input('Digite o novo nome: ')
        idade = int(input('Digite a nova idade: '))

        for informacoes in alunos:
            if (informacoes['id'] == idPessoa):
                informacoes.update({'nome': nome})
                informacoes.update({'idade': idade})
    elif (opcao == 3):
        for informacoes in alunos:      
            print(f"\nID: {informacoes['id']} | Nome: {informacoes['nome']}")

        idPessoa = int(input('Digite o id da pessoa que deseja excluir: '))

        for informacoes in alunos:
            if (informacoes['id'] == idPessoa):
                alunos.remove(informacoes)
    elif (opcao == 4):
        for informacoes in alunos:      
            print(f"\nID: {informacoes['id']} | Nome: {informacoes['nome']} | Rua: {informacoes['rua']} | Cidade: {informacoes['cidade']}")
    else:
        break

print('Fim do programa.')