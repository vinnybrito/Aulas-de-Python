import requests

print('----Conversor de Moedas----')
real = float(input('\nQual o valor em real: '))

print(f'\nDeseja converter para: \n1- Dólar \n2- Euro \n3- Bitcoin')

opcao = int(input('Opção escolhida: '))


if response.status_code == 200:
    if (opcao == 1):
        url = f"https://economia.awesomeapi.com.br/json/last/USD-{real}"

        response = requests.get(url)

        print(f"Dólar: {dados['ask']}")
