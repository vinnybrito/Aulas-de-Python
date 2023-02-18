# 20. Uma escola com cursos em regime semestral realiza duas avaliações durante o 
# semestre e calcula a média do aluno, da seguinte maneira:

#--------------------------- MEDIA = (P1 + 2.P2) / 3 ---------------------------

#Fazer um programa para entrar via teclado com o valor da primeira nota (P1) e o 
# programa deverá calcular e exibir quanto o aluno precisa tirar na segunda nota 
# minimamente (P2) para ser aprovado, sabendo que a média de aprovação é igual a cinco.

p1 = float(input('Digite o valor da primeira nota: '))

p2 = (15 - p1) / 2

print(f'Você precisa tirar no mínimo {p2:.1f} na segunda prova para conseguir a média')
