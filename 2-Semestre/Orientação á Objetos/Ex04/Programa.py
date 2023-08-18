from Conta import Conta
from ContaPoupanca import ContaPoupanca 
from ContaCorrente import ContaCorrente
from ContaSalario import ContaSalario


contas = []

while True:
    print('\n<<--Cadastrar Conta-->>')
    conta = Conta()

    conta.agencia = input('Digite sua agência: ')
    conta.numero = input('Digite o número: ')
    conta.saldo = float(input('Digite o seu saldo: '))

    print('\nEscolha uma opção:')
    print('1- Conta Corrente')
    print('2- Conta Poupança')
    print('3- Conta Salário')
    print('4- Exibir Contas')
    print('5- Sair')

    opcao = int(input('Digite a opção desejada: '))

    if (opcao == 1):
        cc = ContaCorrente()
        cc.checkEspecial = (100)

        dadosConta = {'agencia': conta.agencia, 'numero': conta.numero, 'saldo': conta.saldo, 'check': cc.checkEspecial}

        contas.append(dadosConta)
