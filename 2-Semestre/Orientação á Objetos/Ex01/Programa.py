from Aluno import Aluno

alunos = []
id = 0

def exibirAlunos(formatoCompleto = False):
    if (formatoCompleto):
        for aluno in alunos:      
            print(f"\nID: {aluno.id} | Nome: {aluno.nome} | Idade: {aluno.idade} | RA: {aluno.ra} | Curso: {aluno.curso}")
    else:
        for aluno in alunos:      
            print(f"ID: {aluno.id} | Nome: {aluno.nome}\n")

while True:
    print('\n<<--Cadastro de Alunos-->>')

    print('\nEscolha uma opção:')
    print('1- Incluir Aluno')
    print('2- Alterar')
    print('3- Excluir')
    print('4- Exibir')
    print('5- Sair')

    opcao = int(input('Digite a opção desejada: '))

    if (opcao == 1):
        aluno = Aluno()

        id = id + 1
        aluno.id = id
        aluno.nome = input('Digite o seu nome: ')
        aluno.idade = input('Digite sua idade: ')
        aluno.ra = input('Digite seu RA: ')
        aluno.curso = input('Digite o nome do curso: ')

        alunos.append(aluno)

        print('Aluno cadastrado com sucesso!')

    elif (opcao == 2):
        print('\n<<----Alunos Cadastrados---->>')

        exibirAlunos()

        idAluno = int(input('\nDigite o ID do aluno que deseja atualizar: '))

        nome = input('Digite o novo nome: ')
        idade = int(input('Digite a nova idade: '))
        
        for aluno in alunos:
            if (aluno.id == idAluno):
                aluno.nome = nome
                aluno.idade = idade

    elif (opcao == 3):
        print('\n<<----Alunos Cadastrados---->>')

        exibirAlunos()

        idAluno = int(input('\nDigite o ID do aluno que deseja excluir: '))

        for aluno in alunos:
            if (aluno.id == idAluno):
                alunos.remove(aluno)

    elif (opcao == 4):

        print('\n<<----Alunos Cadastrados---->>')

        exibirAlunos(True)
    else:
        break

print('\nFim do programa.')