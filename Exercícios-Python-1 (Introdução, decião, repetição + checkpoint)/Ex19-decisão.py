# 19. Uma escola com cursos em regime semestral, realiza duas avaliações durante o 
# semestre e calcula a média do aluno, da seguinte maneira:

# ---------------------------- MEDIA = (P1 + 2.P2) / 3 ---------------------------- 

# Fazer um programa para entrar via teclado com os valores das notas (P1 e P2) e 
# calcular a média. Exibir a situação final do aluno (“Aprovado ou Reprovado”), 
# sabendo que a média de aprovação é igual a cinco.

p1 = int(input('Digite o valor da primeira prova: '))

p2 = int(input('Digite o valor da segunda prova: '))

m = (p1 + (2 * p2)) / 3

if (m >= 5):
    print('Aprovado')
else:
    print('Reprovado')
    