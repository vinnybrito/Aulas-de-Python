#30. Elabore um algoritmo que calcule o que deve ser pago por um produto, 
# considerando o preço normal de etiqueta e a escolha da condição de pagamento. 
# Utilize os códigos da tabela a seguir para ler qual a condição de pagamento 
# escolhida e efetuar o cálculo adequado e exibir o valor a ser pago no final.

# Código Condição de pagamento
# 1 - À vista em dinheiro ou cheque, recebe 10% de desconto
# 2 - À vista no cartão de crédito, recebe 15% de desconto
# 3 - Em duas vezes, preço normal de etiqueta sem juros
# 4 - Em quatro vezes, preço normal de etiqueta mais juros de 10%

p = float(input('Digite o valor do produto: '))

fp = input(' 1- Dinheiro ou Cheque\n 2- Cartão de crédito\n 3- Duas parcelas\n 4- Quatro parcelas\n Insira a forma de pagamento: ')

if (fp == '1'):
    d = p - (0.10 * p)
    print(f'Seu desconto é de 10%. O produto custará {d} reais.')
elif (fp == '2'):
    d = p - (0.15 * p)
    print(f'Seu desconto é de 15%. O produto custará {d} reais.')
elif (fp == '3'):
    print(f'Produto sem desconto. O produto custará {p} reais. ')
elif (fp == "4"):
    d = (p * 0.10)
    j = d * 4 + p
    print(f'Produto com juros de 10%. A cada parcela, será cobrado o valor de {d} reais. O valor total a ser pago será de {j} reais.')
else:
    print('Não foi possivel idêntificar a forma de pagamento.')
