
nome = []
sexo = []
idade = []

for i in range(0, 2, 1):
    nome.append(input('Insira o seu nome: '))
    s = input('Insira o seu sexo: ')

    while (s != "f" and s != "m"):
       s = input('Insira o seu sexo: ')
    sexo.append(s)

    age = int(input('Digite sua idade: '))

    while (age < 0):
        age = int(input('Digite sua idade: '))
    idade.append(age)

l = 0

for i in range(0, 2, 1):
    if (idade[i] >= 18):
        print(nome[i])
        print(sexo[i])
        print(idade[i])
        l = l + 1

print("Número de pessoas que mais de 18 anos: ", l)


