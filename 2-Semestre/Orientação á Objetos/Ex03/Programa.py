from Cliente import Cliente
from ContaBancaria import conta

clientes = []

print('<----Cadastro de Clientes---->>')

for i in range (1, 3, 1):
    cli = Cliente()

    id = cli.__len__() + 1
    cli.nome = input('Digite seu nome: ')
    cli.idade = int(input('Digite sua idade: '))
    cli.email = input('Digite seu email: ')

    possuiConta = input('Possuí conta Bancaria? (S/N) ')

    if (possuiConta.upper() == "S"):
        c = conta()

        c.agencia = input("Agência: ")
        c.numero = input("Número: ")
        c.saldo = float(input("Agência: "))

        cli.append(c)
    else:
        cli.append()

    clientes.append(cli)



        