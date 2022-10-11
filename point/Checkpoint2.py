# Armazenar o rm, nome e curso de 5 alunos. Consistir as entradas no sentido de obrigar a digitação de rm e nome. O curso é opcional. Após a digitação, exibir os dados (nome, rm e curso) de todos os alunos.

rm = []
nome = []
cursoid = []
cursonome = []

print('..:: Cadastro de Alunos ::..')

for i in range(0, 5, 1):

    rm.append(int(input("\nDigite o RM: ")))

    nome.append(input("Digite o nome: "))
    
    curso = input('Deseja cadastrar os cursos? (s/n): ')
    if(curso == "s"):
        cursoid.append(int(input("Digite o ID do curso: ")))
        cursonome.append(input('Digite o nome do curso: '))

print("\n..:: Alunos e Cursos ::..")

for i in range(0, 5, 1):
    print("--------------")
    if (curso == "s"):
        print(f'RM: {rm[i]} - {nome[i]} - {cursoid[i]} - {cursonome[i]}')
    else:
        print(f'RM: {rm[i]} - {nome[i]}')
    