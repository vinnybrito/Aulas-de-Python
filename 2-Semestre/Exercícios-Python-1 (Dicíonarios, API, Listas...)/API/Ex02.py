# 2- Crie um programa em Pyhton que permita consultar Devs no GitHub. O programa 
# deve consumir a API do GitHub (Exemplo: https://api.github.com/users/joseffe10), 
# permitindo o usuário digitar algum login do GitHub e após isso retornar as 
# informações.

import requests

github = input('Digite seu nome de usuário do Github: ')
url = f"https://api.github.com/users/{github}"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    
    print(f"\nNome: {dados['name']}")
    print(f"Repositórios: {dados['public_repos']}")
    print(f"Seguidores: {dados['followers']}")
else:
    print("Usuário não encontrado.")