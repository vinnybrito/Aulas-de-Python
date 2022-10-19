# 7. Entrar via teclado com o valor de cinco produtos. Após as entradas, digitar um 
# valor referente ao pagamento da somatória destes valores. Calcular e exibir o troco 
# que deverá ser devolvido.

p1 = float(input('Digite o valor do primeiro produto: '))

p2 = float(input('Digite o valor do segundo produto: '))

p3 = float(input('Digite o valor do terceiro produto: '))

p4 = float(input('Digite o valor do quarto produto: '))

p5 = float(input('Digite o valor do quinto produto: '))

pg = float(input('Digite o valor do pagamento: '))

t = pg - (p1 + p2 + p3 + p4 + p5)

print('O valor do troco a ser devolvido é: ', t)
