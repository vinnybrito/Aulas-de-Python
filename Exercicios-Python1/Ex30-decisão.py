
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
    d = p / (4 * 0.10)
    print(f'Produto com juros de 10%. A cada parcela, será cobrado o valor de {d} reais.')
else:
    print('Não foi possivel idêntificar a forma de pagamento.')
