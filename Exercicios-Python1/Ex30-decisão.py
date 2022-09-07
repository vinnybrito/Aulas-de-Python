
p = float(input('Digite o valor do produto: '))

fp = input(' 1- Dinheiro ou Cheque\n 2- Cartão de crédito\n 3- Duas parcelas\n 4- quatro parcelas\n Insira a forma de pagamento: ')

if (fp == '1'):
    d = p - (0.10 * p)
    print('Seu desconto é de 10%: ', d)
elif (fp == '2'):
    d = p - (0.15 * p)
    print('Seu desconto é de 15% ', d)
elif (fp == '3'):
    print('Produto sem desconto: ', p)
else:
    d = p / 4 * 0.10
    print('em 4 vezes preço normal com juros de 10%: ', d)