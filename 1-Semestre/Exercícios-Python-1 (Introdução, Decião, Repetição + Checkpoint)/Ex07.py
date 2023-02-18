# 7. Entrar via teclado com o valor de cinco produtos. Após as entradas, 
# digitar um valor referente ao pagamento da somatória destes valores. 
# Calcular e exibir o troco que deverá ser devolvido.

p1 = float(input('1- Produto: '))

p2 = float(input('2- Produto: '))

p3 = float(input('3- Produto: '))

p4 = float(input('4- Produto: '))

p5 = float(input('5- Produto: '))

pg = float(input('Digite o valor do pagamento: '))

troco = round(pg - (p1 + p2 + p3 + p4 + p5), 2)

print(f'Troco: {troco}')
