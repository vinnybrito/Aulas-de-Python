# 3- Crie um programa em Python que permita converter o valor de R$ para outras moedas.
# O programa deve consumir a API de Conversão 
# (Documentação: https://docs.awesomeapi.com.br/api-de-moedas), permitindo o usuário 
# digitar o valor em reais e escolher qual o destino da conversão:

import requests

moedas = {1: 'USD', 2: 'EUR', 3: 'BTC'}

print('\n<<------Conversor de Moedas------>>')
valor = float(input('Qual o valor em R$: '))

print('\nDeseja converter para: \n1- Dolar \n2- Euro \n3- Bitcoin')

opcao = int(input('\nOpção escolhida: '))

url = f"https://economia.awesomeapi.com.br/json/last/{moedas[opcao]}-BRL"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    
    valorConvertido = valor / float(dados[moedas[opcao]+"BRL"]['ask'])
    print(f"O valor convertido é: {valorConvertido:.2f}")
