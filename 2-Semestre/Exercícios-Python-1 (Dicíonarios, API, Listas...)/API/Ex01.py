# 1- Crie um programa em Python que permita consultar endereços através de um Cep.
# O programa deve consumir a API do ViaCep (Exemplo: viacep.com.br/ws/01001000/json/), 
# permitindo o usuário digitar o seu cep e obter as informações.

import requests

print('\n<<----SERVIÇO CEP---->>')

cep = input("\nDigite o CEP desejado: ")
url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()   
    print(f"\nLogradouro: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
else:
    print("CEP não encontrado.")