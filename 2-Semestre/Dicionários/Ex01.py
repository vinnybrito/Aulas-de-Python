# 1- Crie um programa para cadastrar clientes (nome, idade, profissao e salario) e 
# pergunte para cada cliente se ele tem ou não contas bancárias. Caso o cliente 
# tenha, permita ele cadastrar os dados das contas bancárias (banco, agência, 
# número). Ao final, exibir todos os clientes e suas respectivas contas bancárias, 
# se houver.

cliente = []

while True:
    print('\n<<----CADASTRO DE CLIENTES---->>')

    nome = input('\nDigite seu nome: ')
    idade = int(input('Digite sua idade: '))
    profissao = input('Digite sua profissão: ')
    salario = float(input('Digite seu salario: '))

    resposta = input('\nPossuí conta bancária? (S/N) ')

    if (resposta.upper() == "S"):
        banco = input("\nBanco: ")
        agencia = input("Agência: ")
        numero = input("Numero: ")
        contaBancaria = {'banco': banco, 'agencia': agencia, 'numero': numero}
    else:
        contaBancaria = {}

    pessoa = {'nome': nome, 'idade': idade, 'profissao': profissao, 'salario': salario, 'conta': contaBancaria}

    cliente.append(pessoa)

    continuar = input('\nDeseja continuar? (S/N): ')
    
    if (continuar.upper() == "N"):
        break

print('\n<<----CLIENTES CADASTRADOS---->>')

for pessoa in cliente:
    print(f"\nNome: {pessoa['nome']} | Idade: {pessoa['idade']} | Profissão: {pessoa['profissao']} | Salário: {pessoa['salario']}")

    if (contaBancaria):
        print(f"Banco: {contaBancaria['banco']} | Agência: {contaBancaria['agencia']} | Número: {contaBancaria['numero']}")
    else:
        print("Cliente não possuí conta bancaria")