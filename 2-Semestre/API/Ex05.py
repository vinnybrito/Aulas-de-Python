# 5- Crie um programa para testar se o nome de um domínio na Web está disponível 
# para criação de um site. Exemplo: joseffe.com.br
# https://brasilapi.com.br/api/registrobr/v1/joseffe.com.br
# Se o campo "status" retornar AVAILABLE, aparecer na tela Domínio disponível, 
# caso contrário, aparecer Domínio já utilizado e exibir a data de expiração.

import requests

dominio = input("Digite um domínio desejado: ")
url = f"https://brasilapi.com.br/api/registrobr/v1/{dominio}"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()

    if (dados['status'] == 'AVAILABLE'):
        print('Dominio disponível')
    else:
        dataFormatada = dados['expires-at'][8:10] + "/" + dados['expires-at'][5:7] + "/" + dados['expires-at'][0:4]
        
        print('Domínio indisponível! Expira em: ' + dataFormatada)
