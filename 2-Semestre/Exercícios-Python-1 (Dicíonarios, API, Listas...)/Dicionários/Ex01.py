# 1- Crie um programa para cadastrar clientes (nome, idade, profissao e salario) e 
# pergunte para cada cliente se ele tem ou não contas bancárias. Caso o cliente 
# tenha, permita ele cadastrar os dados das contas bancárias (banco, agência, 
# número). Ao final, exibir todos os clientes e suas respectivas contas bancárias, 
# se houver.

cliente = [] # Criamos uma lista, que será responsavel por armazenar os dicionários

while True: # "Enquanto for verdade" - será realizado um looping infinito.
    print('\n<<------Cadastro de Úsuarios------>>')
    print('Por favor, digite os seus dados: ')
    nome = input('\nNome: ')
    idade = int(input('Idade: '))
    profissao = input('Profissão: ')
    salario = float(input('Salário: '))

    conta = input('\nPossui conta bancária? (S/N) ')
    
    if (conta.upper() == "S"):
        banco = input('\nBanco: ')
        agencia = input('Agência: ')
        numero = input('Número: ')

        contabancaria = {'banco': banco, 'agencia': agencia, 'numero': numero}
        #Criar dicionário

        print('\nCadastrado com Sucesso!')
    else:
        contabancaria = {}
        print('\nCadastrado com Sucesso!')

    dado = {'nome': nome, 'idade': idade, 'profissao': profissao, 'salario': salario, 'conta': contabancaria}
    #Criar dicionário e adionar outro dicionario.

    cliente.append(dado)

    continuar = input("\nDeseja continuar? (S/N) ")
    if continuar.upper() == "N":
        break

for dado in cliente:
    print(f"\nNome: {dado['nome']} | Idade: {dado['idade']} | Profissão: {dado['profissao']} | Salário: {dado['salario']}")

    if (contabancaria):
        print(f"Banco: {contabancaria['banco']} | Agência: {contabancaria['agencia']} | Número: {contabancaria['numero']}")
    else:
        print("Cliente não possui conta bancária.")