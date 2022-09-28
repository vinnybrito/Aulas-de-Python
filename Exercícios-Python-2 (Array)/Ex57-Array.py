
nome = []
sexo = []
idade = []

for i in range(0, 5, 1):
    nome.append(input('Insira o seu nome: '))
    s = input('Insira o seu sexo: ')

    while (s != "f" and s != "m"):
       s = input('Insira o seu sexo: ')
    sexo.append(s)

    age = int(input('Digite sua idade: '))

    while (age < 0):
        age = int(input('Digite sua idade: '))
    idade.append(age)


for i in range(0, 5, 1):
    if (sexo[i] == "f"):
        print(nome[i])
        print(sexo[i])
        print(idade[i])