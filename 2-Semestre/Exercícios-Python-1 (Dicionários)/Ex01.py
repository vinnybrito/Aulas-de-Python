# 1- Crie um programa para cadastrar clientes (nome, idade, profissao e salario) e 
# pergunte para cada cliente se ele tem ou não contas bancárias. Caso o cliente 
# tenha, permita ele cadastrar os dados das contas bancárias (banco, agência, 
# número). Ao final, exibir todos os clientes e suas respectivas contas bancárias, 
# se houver.

clientes = []

while True:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    profissao = input("Digite a profissão: ")
    salario = float(input("Digite o salário: "))

    contabancaria = input("\nPossui conta bancária? (S/N): ")

    if (contabancaria.upper() == "S"):

        banco = input("\nDigite nome do banco: ")
        agencia = int(input("Digite o número da agência: "))
        numero = int(input("Digite o número: "))

        contabancaria = {"banco": banco, "agencia": agencia, "numero": numero}
    else:
        contabancaria = {}

    pessoa = {"nome": nome, "idade": idade, "profissão": profissao,"salario": salario, "conta": contabancaria}

    clientes.append(pessoa)

    continuar = input("\nDeseja continuar? (S/N) ")
    if continuar.upper() == "N":
        break

for pessoa in clientes:
    print(f"\nNome: {pessoa['nome']} | Idade: {pessoa['idade']} | Salário: {pessoa['salario']}")

    if (contabancaria):
        print(f"Banco: {contabancaria['banco']} | Agência: {contabancaria['agencia']} | Número: {contabancaria['numero']}")
    else:
        print("Cliente não possui conta bancária.")
